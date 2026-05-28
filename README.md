NAMA:M.ASROR RAMDHANI

NIM:22250019

📘 Praktikum Python — Struktur Data

📂 Daftar Program
Repository ini berisi tugas praktikum Python mengenai implementasi struktur data sederhana menggunakan:

• Set
• Linked List

───

📨 Program 1— Filter Email Spam

Program ini digunakan untuk mendeteksi email spam menggunakan struktur data set.
 Sistem akan memeriksa apakah isi email mengandung kata-kata yang termasuk spam seperti promo, diskon, hadiah, dan gratis.

Jika ditemukan kata spam, maka email dianggap sebagai spam.

───

✨ Fitur Program
• Input email dari pengguna
• Deteksi kata spam otomatis
• Menggunakan operasi intersection()
• Menampilkan kata spam yang ditemukan

🎵 Program 2 — Playlist Musik Menggunakan Linked List

Program ini mensimulasikan daftar putar musik sederhana menggunakan struktur data Linked List.

Pada program ini, setiap lagu disimpan dalam sebuah node yang saling terhubung satu sama lain.
 Setiap node memiliki:
• Data lagu
• Pointer (next) menuju lagu berikutnya

Konsep ini mirip seperti playlist pada aplikasi pemutar musik, di mana lagu diputar secara berurutan.

───

🧩 Penjelasan Struktur Program

📌 Class Node

Class Node digunakan untuk menyimpan data lagu dan alamat menuju node berikutnya.

python
class Node:
    def __init__(self, lagu):
        self.lagu = lagu
        self.next = None



