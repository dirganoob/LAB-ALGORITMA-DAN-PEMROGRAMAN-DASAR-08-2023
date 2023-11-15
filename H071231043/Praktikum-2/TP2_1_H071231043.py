gender = int(input("Pilih Gender Anda \n1. Pria \n2. Wanita \n= "))

tinggiBadan = float(input("Masukkan tinggi badan (cm) : "))
beratBadan = float(input("Masukkan berat badan (kg) : "))

BMI = beratBadan / (tinggiBadan / 100) ** 2

if gender == 1:
    if BMI < 18:
        kategori = "Underweight"
    elif 18 <= BMI <= 23.9:
        kategori = "Normal"
    elif 24 <= BMI <= 26.9:
        kategori = "Overweight"
    else:
        kategori = "Obese"
    print(f"Anda tergolong {kategori} dengan BMI {BMI:.2f}")
elif gender == 2:
    if BMI < 17:
        kategori = "Underweight"
    elif 17 <= BMI <= 23.9:
        kategori = "Normal"
    elif 24 <= BMI <= 27.9:
        kategori = "Overweight"
    else:
        kategori = "Obese"
    print(f"Anda tergolong {kategori} dengan BMI {BMI:.2f}")
else:
    print("Mohon pilih 1 atau 2")