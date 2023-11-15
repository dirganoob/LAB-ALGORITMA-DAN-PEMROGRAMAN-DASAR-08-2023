uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

total_harga = int(input(": "))
jumlah_uang = int(input(": "))

# Menghitung kembalian
kembalian = jumlah_uang - total_harga

if kembalian < 0:
    print("Maaf, uang yang diberikan tidak mencukupi.")
else:
    print("Kembalian:")
    for pecahan in uang_pecahan:
        jumlah_pecahan = kembalian // pecahan
        print(f"{jumlah_pecahan} uang sejumlah Rp. {pecahan}")
        kembalian -= jumlah_pecahan * pecahan
