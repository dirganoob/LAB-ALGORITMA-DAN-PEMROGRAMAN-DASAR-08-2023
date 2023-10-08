
while True:
    posisi = float(input('Masukkan derajat posisi matahari : '))

    menit = (posisi / 360) * 24 * 60
    jam = (menit // 60) + 6 #ditambah 6 karena 0 derajat pada jam 6
    if jam >= 24:
        jam %= 24 #jika melebihi jam 24:00:00 akan mulai lagi jam 00:00:00
    detik = (menit * 60) % 60
    menit = menit % 60

    if 6 <= jam < 10 :
        print('\nSelamat Pagi')
    elif 10 <= jam < 15:
        print('\nSelamat Siang')
    elif 15 <= jam < 18:
        print('\nSelamat Sore')
    elif 18 <= jam < 24 or 0 <= jam < 6:
        print('\nSelamat Malam') 

    print(f'{jam:02.0f}:{menit:02.0f}:{detik:02.0f}\n')
