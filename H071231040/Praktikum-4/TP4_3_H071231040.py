def maksimum(*angka):
    maks = angka[0]
    for angka_terbesar in angka:
        if angka_terbesar > maks:
            maks = angka_terbesar
    
    return maks

print(f'>> {maksimum(1, 2, 4, 6, 9, 3, 1, 9, 10)}')
print(f'>> {maksimum(0, 1, 90, 430, 23, 212, 34)}')
print(f'>> {maksimum(37, 84, 29, 51, 12)}')