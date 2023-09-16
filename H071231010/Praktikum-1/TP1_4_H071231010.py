# Input karakter
karakter = input("karakter: ")

# Inisialisasi variabel
is_huruf_kapital = False
is_huruf_kecil = False
is_angka = False

# Memeriksa karakter
if karakter.isupper(): 
    is_huruf_kapital = True
if karakter.islower():
    is_huruf_kecil = True
if karakter.isdigit():
    is_angka = True

# Menampilkan hasil
print(f'Huruf kapital?: {is_huruf_kapital}')
print(f'Huruf kecil?: {is_huruf_kecil}')
print(f'Angka?: {is_angka}')