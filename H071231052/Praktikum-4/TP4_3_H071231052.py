def maksimum(*daftar):
    try:
        angka_terbesar = daftar[0]

        for angka in daftar:
            if angka > angka_terbesar:
                angka_terbesar = angka
        return angka_terbesar

    except IndexError as err:
        print(err)
angka_max = maksimum(1,2,3,4,5,6,7,5,4,3,2,2,3,1)

print(f"Angka maksimum dari bilangan tersebut adalah {angka_max}")