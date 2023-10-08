harga = int(input('Masukkan harga barang : '))
bayar = int(input('Masukkan Nominal uang anda : '))
kembalian = bayar - harga
uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
jumlah = 0

if harga <= bayar:
    for pecahan in uang:
        jumlah = kembalian // pecahan
        kembalian = kembalian % pecahan
        print(f'{jumlah} uang sejumlah Rp. {pecahan}')
else:
    print('Uang anda tidak cukup, pinjam dulu 100')