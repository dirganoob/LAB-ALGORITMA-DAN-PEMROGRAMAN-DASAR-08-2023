# Input sisi X dan Y
sisi_x = float(input("panjang sisi X: "))
sisi_y = float(input("panjang sisi Y: "))

# Menghitung sisi Z menggunakan teorema Pythagoras
sisi_z = (sisi_x ** 2 + sisi_y ** 2) ** 0.5

# Menghitung luas segitiga
luas_segitiga = 0.5 * sisi_x * sisi_y

# Menghitung keliling segitiga
keliling_segitiga = sisi_x + sisi_y + sisi_z

# Menampilkan hasil dengan dua angka di belakang koma
print(f"Luas permukaan: {luas_segitiga:.2f}")
print(f"Keliling: {keliling_segitiga:.2f}")