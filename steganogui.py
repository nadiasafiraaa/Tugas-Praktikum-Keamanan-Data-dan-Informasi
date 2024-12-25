from stegano import lsb
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, Canvas
import os


class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Tool")
        self.root.geometry("600x400")
        self.root.minsize(600, 400)  # Ukuran minimum
        self.root.resizable(True, True)  # Jendela dapat diubah ukurannya

        # Latar belakang gradient
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill="both", expand=True)
        self.create_gradient("#cce7ff", "#ffffff")  # Gradient dari biru muda ke putih

        # Gaya elemen GUI
        style = ttk.Style()
        style.configure("TLabel", background="#cce7ff", foreground="black", font=("Arial", 14))
        style.configure("TButton", font=("Arial", 12, "bold"), padding=5, foreground="black")
        style.map("TButton", background=[("active", "#70a1ff"), ("!active", "#1e90ff")])

        # Header
        self.title_label = ttk.Label(
            self.root, text="Steganography Tool", font=("Arial", 24, "bold"), background="#cce7ff"
        )
        self.title_label.place(relx=0.5, y=30, anchor="center")

        # Tombol utama
        self.hide_button = ttk.Button(
            self.root, text="Sembunyikan Pesan", command=self.hide_message, width=25
        )
        self.hide_button.place(relx=0.5, rely=0.3, anchor="center")

        self.reveal_button = ttk.Button(
            self.root, text="Tampilkan Pesan", command=self.reveal_message, width=25
        )
        self.reveal_button.place(relx=0.5, rely=0.45, anchor="center")

        self.exit_button = ttk.Button(
            self.root, text="Keluar", command=self.root.quit, width=25
        )
        self.exit_button.place(relx=0.5, rely=0.6, anchor="center")

        # Footer
        self.footer_label = ttk.Label(
            self.root,
            text="Dibuat oleh Nadia Safira dengan NIM 220705077",
            font=("Arial", 10),

            foreground="black",
        )
        self.footer_label.place(relx=0.5, rely=0.9, anchor="center")

        # Bind ukuran jendela untuk memperbarui elemen GUI
        self.root.bind("<Configure>", self.on_resize)

    def create_gradient(self, color1, color2):
        """Membuat latar belakang gradient."""
        self.canvas.delete("gradient")  # Hapus gradient sebelumnya
        steps = 100
        for i in range(steps):
            r1, g1, b1 = self.hex_to_rgb(color1)
            r2, g2, b2 = self.hex_to_rgb(color2)
            r = r1 + (r2 - r1) * i // steps
            g = g1 + (g2 - g1) * i // steps
            b = b1 + (b2 - b1) * i // steps
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_rectangle(0, i * (self.root.winfo_height() // steps), self.root.winfo_width(),
                                         (i + 1) * (self.root.winfo_height() // steps), outline="", fill=color, tags="gradient")

    @staticmethod
    def hex_to_rgb(hex_color):
        """Mengonversi kode warna HEX menjadi RGB."""
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    def on_resize(self, event):
        """Memperbarui gradient dan posisi elemen saat ukuran jendela berubah."""
        self.create_gradient("#cce7ff", "#ffffff")  # Perbarui gradient
        self.title_label.place(relx=0.5, y=30, anchor="center")
        self.hide_button.place(relx=0.5, rely=0.3, anchor="center")
        self.reveal_button.place(relx=0.5, rely=0.45, anchor="center")
        self.exit_button.place(relx=0.5, rely=0.6, anchor="center")
        self.footer_label.place(relx=0.5, rely=0.9, anchor="center")

    def hide_message(self):
        # Menyembunyikan pesan
        img_path = filedialog.askopenfilename(
            title="Pilih Gambar",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")]
        )
        if not img_path:
            return

        message = tk.simpledialog.askstring("Masukkan Pesan", "Masukkan pesan yang ingin disembunyikan:")
        if not message:
            return

        save_path = filedialog.asksaveasfilename(
            title="Simpan Gambar",
            defaultextension=".png",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")]
        )
        if not save_path:
            return

        try:
            secret = lsb.hide(img_path, message)
            secret.save(save_path)
            messagebox.showinfo("Berhasil", f"Gambar berhasil disimpan di {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyembunyikan pesan: {e}")

    def reveal_message(self):
        # Menampilkan pesan
        img_path = filedialog.askopenfilename(
            title="Pilih Gambar",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")]
        )
        if not img_path:
            return

        try:
            clear_message = lsb.reveal(img_path)
            if clear_message:
                messagebox.showinfo("Pesan Tersembunyi", f"Pesan: {clear_message}")
            else:
                messagebox.showinfo("Tidak Ada Pesan", "Tidak ada pesan tersembunyi dalam gambar.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membaca gambar: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
