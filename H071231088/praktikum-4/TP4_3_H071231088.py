def maksimum(*a):
    angka_terbesar = a[0]
    for angka in a:
        if angka > angka_terbesar:
            angka_terbesar = angka
    return angka_terbesar

angka = maksimum(1, 2, 4, 6, 9, 3, 1, 9, 10)
print(angka)