print("konversi suhu dari celsius ke kelvin, reamur, dan fahrenheit")

cel = int(input("masukkan suhu dalam celsius: "))

fah = (9/5 * cel) + 32
rea = cel * 4/5 
kel = cel + 273.15

print(f"hasil konversi dari suhu {cel} Celsius ke kelvin adalah: {kel}K ")
print(f"hasil konversi dari suhu {cel} Celsius ke Reamur adalah: {rea}R ")
print(f"hasil konversi dari suhu {cel} Celsius ke Fahrenheit adalah: {fah}F ")