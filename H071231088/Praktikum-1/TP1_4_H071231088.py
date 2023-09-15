print("pengujian jenis karakter")
karakter = input("karakter = ")
kapital = 'A' <= karakter <= 'Z'
kecil = 'a' <= karakter <= 'z'
angka = '0' <= karakter <= '9'

print(f"Huruf kapital? {kapital}")
print(f"Huruf kecil? {kecil}")
print(f"Angka? {angka}")