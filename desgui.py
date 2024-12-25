import tkinter as tk
from tkinter import messagebox, scrolledtext
from Crypto.Cipher import DES
import base64


def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


# Fungsi Enkripsi
def encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')


# Fungsi Dekripsi
def decrypt(encrypted_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = des.decrypt(decoded_encrypted_text).decode('UTF-8')
    return decrypted_text.rstrip()


class DESEncryptionApp:
    def __init__(self, master):
        self.master = master
        master.title("DES Encryption/Decryption")
        master.geometry("800x600")
        master.configure(bg="#2c3e50")

        # Header
        self.header = tk.Label(
            master,
            text="DES Encryption/Decryption",
            font=("Arial", 22, "bold"),
            bg="#34495e",
            fg="white",
            padx=10,
            pady=15,
        )
        self.header.pack(fill=tk.X)

        # Frame utama
        self.main_frame = tk.Frame(master, bg="#2c3e50")
        self.main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Key Input
        self.label_key = tk.Label(
            self.main_frame, text="Key (8 characters):", font=("Arial", 14), bg="#2c3e50", fg="white", anchor="w"
        )
        self.label_key.grid(row=0, column=0, sticky="w", pady=10, padx=10)
        self.entry_key = tk.Entry(
            self.main_frame, show="*", font=("Arial", 14), width=30, bg="#ecf0f1", relief="flat"
        )
        self.entry_key.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

        # Data Input
        self.label_data = tk.Label(
            self.main_frame, text="Plaintext:", font=("Arial", 14), bg="#2c3e50", fg="white", anchor="w"
        )
        self.label_data.grid(row=1, column=0, sticky="w", pady=10, padx=10)
        self.entry_data = tk.Entry(
            self.main_frame, font=("Arial", 14), width=30, bg="#ecf0f1", relief="flat"
        )
        self.entry_data.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

        # Buttons
        self.button_frame = tk.Frame(self.main_frame, bg="#2c3e50")
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=20)

        self.button_encrypt = tk.Button(
            self.button_frame,
            text="Encrypt",
            font=("Arial", 14),
            command=self.encrypt,
            bg="#27ae60",
            fg="white",
            width=12,
            relief="flat",
        )
        self.button_encrypt.pack(side=tk.LEFT, padx=10)

        self.button_decrypt = tk.Button(
            self.button_frame,
            text="Decrypt",
            font=("Arial", 14),
            command=self.decrypt,
            bg="#2980b9",
            fg="white",
            width=12,
            relief="flat",
        )
        self.button_decrypt.pack(side=tk.LEFT, padx=10)

        # Result Display
        self.label_result = tk.Label(
            self.main_frame, text="Result:", font=("Arial", 14), bg="#2c3e50", fg="white"
        )
        self.label_result.grid(row=3, column=0, sticky="nw", pady=10, padx=10)
        self.text_result = scrolledtext.ScrolledText(
            self.main_frame,
            height=10,
            wrap=tk.WORD,
            font=("Arial", 14),
            bg="#ecf0f1",
            relief="flat",
        )
        self.text_result.grid(row=3, column=1, pady=10, padx=10, sticky="nsew")

        # Grid Weighting for Responsiveness
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=2)
        self.main_frame.grid_rowconfigure(3, weight=1)

    def encrypt(self):
        key_input = self.entry_key.get()
        plain_text = self.entry_data.get()

        if len(key_input) != 8:
            messagebox.showerror("Error", "Key must be 8 characters long.")
            return

        key = key_input.encode('utf-8')
        encrypted_text = encrypt(plain_text, key)

        self.text_result.delete(1.0, tk.END)
        self.text_result.insert(tk.END, f"Encrypted Text: {encrypted_text}")

    def decrypt(self):
        key_input = self.entry_key.get()
        encrypted_text = self.text_result.get(1.0, tk.END).strip()

        if len(key_input) != 8:
            messagebox.showerror("Error", "Key must be 8 characters long.")
            return

        if not encrypted_text.startswith("Encrypted Text: "):
            messagebox.showerror("Error", "Invalid encrypted text format.")
            return

        encrypted_text = encrypted_text.replace("Encrypted Text: ", "")
        key = key_input.encode('utf-8')
        decrypted_text = decrypt(encrypted_text, key)

        self.text_result.delete(1.0, tk.END)
        self.text_result.insert(tk.END, f"Decrypted Text: {decrypted_text}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DESEncryptionApp(root)
    root.mainloop()
