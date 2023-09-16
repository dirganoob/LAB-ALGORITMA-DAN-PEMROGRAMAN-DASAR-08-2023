# Input detik
detik = int(input("Masukkan jumlah detik: "))

# Menghitung jam, menit, dan sisa detik
jam = detik // 3600
menit = detik % 3600 //60
detik_sisa = detik % 60

# Menampilkan hasil konversi dalam format yang diinginkan
print(f"Hasil konversi: {jam:02d}:{menit:02d}:{detik_sisa:02d}")