print("menghitung luas dan keliling segitga")

X = float(input("panjang sisi X ="))
Y = float(input("panjang sisi Y ="))
Z = (Y**2 + X**2)**0.5

L= 1/2 * Y * X
keliling = Y + X + Z

print("luas segitiga adalah = ", round(L,2))
print("keliling segitiga = ", round(keliling, 2))