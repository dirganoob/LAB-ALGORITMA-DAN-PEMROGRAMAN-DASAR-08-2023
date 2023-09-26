# #NOMOR 01
# masukkan jenis kelamin kelamin
print("Pilih Gender Anda")
print("1. Pria")
print("2. Wanita")
jenis_kelamin = int(input("= "))

# Input tinggi dan berat badan
tinggi = float(input("Masukkan tinggi badan (cm): "))
berat = float(input("Masukkan berat badan (kg): "))

#rumus (tinggi di konversi ke meter dengan membagi tinggi ke 100)
BMI =  berat / (tinggi/100)**2

#jenis kelamin pria
if jenis_kelamin == 1:
    if BMI < 18:
        status = "Underweight"
    elif 18 <= BMI < 23.9:
        status = "Normal"
    elif 24 <=BMI < 26.9:
        status = "Overweight"
    elif BMI >= 27:
        status = "Obese"

#jenis kelamin wanita
elif jenis_kelamin == 2:
    if BMI < 17:
        status = "Kurus"
    elif 17 <= BMI < 23.9:
        status = "Normal"
    elif 24 <=BMI < 27.9:
        status = "Gemuk"
    elif BMI >= 28:
        status = "Obesitas"

#hasil
print(f"Anda tergolong {status} dengan BMI {BMI:.2f} ")





