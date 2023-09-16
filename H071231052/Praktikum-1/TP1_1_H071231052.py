x = float(input('Masukkan nilai X : '))
y = float(input('Masukkan nilai Y : '))
z = (x**2 + y**2)**0.5

luas = 0.5 * x * y
keliling = x + y + z

print(f'luas permukaan : {luas:.2f}')
print(f'keliling : {keliling:.2f}')
