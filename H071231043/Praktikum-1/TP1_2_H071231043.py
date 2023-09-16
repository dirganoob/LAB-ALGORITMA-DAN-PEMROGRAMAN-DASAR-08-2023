celcius = int(input("Masukkan suhu dalam Celcius: "))

kelvin = int(celcius + 273.15)
reamur = int((4/5) * celcius)
fahrenheit = int((celcius * 9/5) + 32)

print(f"hasil konversi dari suhu {celcius} derajat celcius ke kelvin adalah: {kelvin}K")
print(f"hasil konversi dari suhu {celcius} derajat celcius ke reamur adalah: {reamur}R")
print(f"hasil konversi dari suhu {celcius} derajat celcius ke fahrenheit adalah: {fahrenheit}F")