print('Konversi jumlah detik ke jam')
nilai_input = int(input('Masukkan jumlah detik : '))

jam = nilai_input // 3600
if jam == 0:
    menit = nilai_input // 60
    detik = nilai_input % 60
else: 
    detik = nilai_input % (jam * 3600)
    menit = detik // 60
    detik %= 60  

print(f'{jam:02}:{menit:02}:{detik:02}')