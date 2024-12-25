import tkinter as tk
from tkinter import messagebox


# Fungsi untuk enkripsi
def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text


# Fungsi untuk dekripsi
def dekripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            plain_text += char
    return plain_text


# Fungsi untuk menangani tombol enkripsi
def handle_enkripsi():
    plain_text = entry_plain.get()
    shift = entry_shift.get()
    if not shift.isdigit():
        messagebox.showerror("Error", "Nilai pergeseran harus berupa angka.")
        return
    shift = int(shift) % 26
    cipher_text = enkripsi(plain_text, shift)
    entry_cipher.delete(0, tk.END)
    entry_cipher.insert(0, cipher_text)


# Fungsi untuk menangani tombol dekripsi
def handle_dekripsi():
    cipher_text = entry_cipher.get()
    shift = entry_shift.get()
    if not shift.isdigit():
        messagebox.showerror("Error", "Nilai pergeseran harus berupa angka.")
        return
    shift = int(shift) % 26
    plain_text = dekripsi(cipher_text, shift)
    entry_plain.delete(0, tk.END)
    entry_plain.insert(0, plain_text)


# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Caesar Cipher")
root.geometry("500x300")
root.configure(bg="#001F3F")  # Warna navy untuk latar belakang

# Judul aplikasi
title_label = tk.Label(
    root,
    text="Aplikasi Caesar Cipher",
    font=("Arial", 16, "bold"),
    bg="#001F3F",
    fg="white",
)
title_label.pack(pady=10)

# Frame untuk form
form_frame = tk.Frame(root, bg="#001F3F")
form_frame.pack(pady=10, padx=10)

# Label dan Entry untuk teks asli (plaintext)
label_plain = tk.Label(
    form_frame, text="Teks Asli (Plaintext):", font=("Arial", 12), bg="#001F3F", fg="white"
)
label_plain.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_plain = tk.Entry(form_frame, width=40, font=("Arial", 12))
entry_plain.grid(row=0, column=1, padx=10, pady=5)

# Label dan Entry untuk nilai pergeseran (shift)
label_shift = tk.Label(
    form_frame, text="Nilai Pergeseran (Shift):", font=("Arial", 12), bg="#001F3F", fg="white"
)
label_shift.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_shift = tk.Entry(form_frame, width=10, font=("Arial", 12))
entry_shift.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Label dan Entry untuk teks terenkripsi (ciphertext)
label_cipher = tk.Label(
    form_frame, text="Teks Terenkripsi (Ciphertext):", font=("Arial", 12), bg="#001F3F", fg="white"
)
label_cipher.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_cipher = tk.Entry(form_frame, width=40, font=("Arial", 12))
entry_cipher.grid(row=2, column=1, padx=10, pady=5)

# Tombol Enkripsi dan Dekripsi
button_frame = tk.Frame(root, bg="#001F3F")
button_frame.pack(pady=10)

button_encrypt = tk.Button(
    button_frame,
    text="Enkripsi",
    command=handle_enkripsi,
    font=("Arial", 12),
    bg="#004080",
    fg="white",
    width=15,
)
button_encrypt.grid(row=0, column=0, padx=10, pady=5)

button_decrypt = tk.Button(
    button_frame,
    text="Dekripsi",
    command=handle_dekripsi,
    font=("Arial", 12),
    bg="#004080",
    fg="white",
    width=15,
)
button_decrypt.grid(row=0, column=1, padx=10, pady=5)

# Menjalankan aplikasi
root.mainloop()
