print('Pengujian jenis karakter\n-----------------------')
karakter = input('Masukkan karakter : ')

kapital = karakter.isupper()
kecil = karakter.islower()
angka = karakter.isnumeric()

print(f'Huruf kapital? {kapital}')
print(f'Huruf kecil? {kecil}')
print(f'Huruf angka? {angka}')
