def palindrom(kalimat):
    kalimat = kalimat.lower()
    kalimat_reverse = "".join(reversed(kalimat))
    if kalimat == kalimat_reverse:
        return "Palindrom"
    else:
        return "Bukan Palindrom"

teks = input("Masukkan Kata : ")
output = palindrom(teks)
print(f'Kata "{teks}" adalah {output}')