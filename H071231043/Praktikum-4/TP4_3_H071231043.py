def maksimum_angka (*angka):
    angka_terbesar = angka[0]

    for i in angka:
        if i > angka_terbesar:
            angka_terbesar = i

    return angka_terbesar

# case1
daftarAngka = [0, 1, 90, 430, 23, 212, 34]
print(">>", maksimum_angka(daftarAngka))