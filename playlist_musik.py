print("=" * 5, "DAFTAR PUTAR MUSIK", "=" * 5)

# Membuat node
class Node:
    def __init__(self, lagu):
        self.lagu = lagu
        self.next = None

# Membuat linked list
class Playlist:
    def __init__(self):
        self.head = None

    # Menambah lagu
    def tambah_lagu(self, lagu):
        baru = Node(lagu)

        if self.head is None:
            self.head = baru
        else:
            sekarang = self.head
            while sekarang.next:
                sekarang = sekarang.next
            sekarang.next = baru

    # Menampilkan playlist
    def tampilkan(self):
        sekarang = self.head

        if sekarang is None:
            print("Playlist kosong")
        else:
            while sekarang:
                print("- ", sekarang.lagu)
                sekarang = sekarang.next

# Program utama
playlist = Playlist()

playlist.tambah_lagu("Hymne Guru")
playlist.tambah_lagu("Indonesia Raya")
playlist.tambah_lagu("Laskar Pelangi")

print("\nDaftar Lagu:")
playlist.tampilkan()
