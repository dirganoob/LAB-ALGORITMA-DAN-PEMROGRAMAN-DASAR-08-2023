#  soal nomor 1 menghintung luas dan keliling Segitiga X , Y , Z :

# print ('menghitung luas dan keliling segitiga')
# x = float(input('panjang sisi x =  '))
# y = float(input('panjang sisi y =  '))
# Z = (x**2 + y**2)**0.5 


# L = x * y / 2
# K = x + y + Z
# print(f'luas permukaan : {L: .2f}')
# print(f'keliling : {K: .2f}')


# soal nomor 2 mengkonversi suhu celcius ke kelvin, reamur, dan farenheit :

# print('konversi suhu dari celcius ke kelvin, reamur, farenheit')
# c = int(input('masukkan suhu dalam celcius:  '))
# K = int(c + 273)
# R = int(4/5 * c)
# F = int((c* 9/5) + 32)

# print (f'hasil konversi dari suhu {c} derajat celcius ke kelvin adalah:      {K}K')
# print (f'hasil konversi dari suhu {c} derajat celcius ke reamur adalah :     {R}R')
# print (f'hasil konversi dari suhu {c} derajat celcius ke farenheit adalah :  {F}F')


# soal nomor 3 membuat program untuk menghitung solusi persamaan kuadrat 
#     ax**2 + bx + c = 0 dengan nilai a , b , dan c sebgai inputan dan nilai x sebagai output pada program
    # niali x yang memenuhi:
# a =  float(input('input a = '))
# if a == 0:
#     print("input a tidak boleh 0  ")
#     exit()

# b =  float(input('input b = '))
# c =  float(input('input c = '))


# x1 = (-b + ((b**2 - 4*a*c)**0.5))/(2*a)
# x2 = (-b - ((b**2 - 4*a*c)**0.5))/(2*a)

# print(f'x1 = {x1:.2f}')
# print(f'x2 = {x2:.2f}')

# soal nomor 4  membuat program untuk menentukan karakter huruf kapital, huruf kecil , dan angka dari inputan yang di lemparkan :

print('pengujian karakter huruf kapital')

k = input("KARAKTER = ")
Kapital = 'A'<=k<'Z'
kecil = 'a' <=k<= 'z'
angka = '0'<= k <='9'


print ("huruf kapital?",Kapital)
print ("huruf kecil?",kecil)
print ("angka?",angka)


# soal nomor 5 merubah detik ke dalam format jam : menit : detik 
# print('konversi detik ke jam ')
# detik = int(input('masukkan jumlah detik: '))

# jam = detik // 3600
# menit = detik % 3600 // 60
# detik = detik % 60

# print(f"{jam:02d}:{menit:02d}:{detik:02d}")