golongan = input("Golongan = ")
daya =int(input("Daya = "))
pemakaian =int(input("Pemakaian = "))

if golongan == 'R1':
    if daya == 900:
        tarif = 1352
    elif daya == 1300 or daya == 2200:
        tarif = 1444.70
elif golongan == 'R2':
    3500 <= daya <= 5500
    tarif = 1699.53
elif golongan == 'R3':
    daya >= 6600
    tarif = 1699.53
elif golongan == 'B2':
    6600 <= daya <= 200000
    tarif = 1444.70
elif golongan == 'B3':
    daya > 200000
    tarif = 1114.74
elif golongan == 'I3':
    daya >= 200000
    tarif = 1314.12
elif golongan == 'P1':
    6600 <= daya <= 200000
    tarif = 1523.28
else:
    print("data tidak valid")
    exit()

tagihan = tarif * pemakaian
tagihan_baru = f"{tagihan:,.1f}".replace(',','.')
print(f"Jumlah tagihan anda : Rp. {tagihan_baru}")