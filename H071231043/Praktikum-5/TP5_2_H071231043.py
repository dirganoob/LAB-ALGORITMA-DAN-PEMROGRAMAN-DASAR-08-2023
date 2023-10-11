def ATH(karakter):
    panjang = len(karakter)
    
    if panjang % 2 == 0:
        hasil = "Jumlah genap tidak dapat dicari tengahnya"
        return hasil
    else:
        awal = karakter[0]
        tengah = karakter[panjang // 2]
        akhir = karakter[-1]
        hasil = f"{awal}{tengah}{akhir}"

        return hasil

kata = input("Masukkan kata: ").replace(" ", "")

hasil_string = ATH(kata)
print(hasil_string)