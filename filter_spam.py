print("=" * 5, "PROGRAM FILTER SPAM", "=" * 5)

# Kata-kata yang dianggap spam
kata_spam = {"promo", "diskon", "hadiah", "gratis", "voucher"}

# Input email
email = input("Masukkan isi email: ").lower()

# Pisahkan kata dalam email menjadi set
kata_email = set(email.split())

# Cek apakah ada kata spam
hasil = kata_spam.intersection(kata_email)

if hasil:
    print("Email terdeteksi SPAM")
    print("Kata spam ditemukan:", hasil)
else:
    print("Email aman")
