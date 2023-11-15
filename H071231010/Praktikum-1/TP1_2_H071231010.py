celcius = int(input("masukkan suhu dalam celcius: "))

kelvin = int(celcius + 273.5)
reamur = int((4/5) * celcius)
fahrenheit = int((celcius * 9/5) + 32)

print(f"Hasil konversi dari suhu {celcius} derajat celcius ke kelvin adalah : {kelvin}K")
print(f"Hasil konversi dari suhu {celcius} derajat celcius ke Reamur adalah : {reamur}R")
print(f"Hasil konversi dari suhu {celcius} derajat celcius ke Fahrenheit adalah: {fahrenheit}F")