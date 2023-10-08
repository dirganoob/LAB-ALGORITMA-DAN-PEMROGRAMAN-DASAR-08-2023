banyakSuku = int(input('Masukkan suku : '))
suku = 0
n1 = 0
n2 = 1

while suku < banyakSuku:
    print(n1, end=' ')
    akhir = n1 + n2
    n1 = n2
    n2 = akhir
    suku += 1