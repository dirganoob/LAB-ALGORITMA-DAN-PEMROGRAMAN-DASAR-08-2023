pilihan = int(input('Pilih gender anda\n1. Pria\n2. Wanita\n= '))

tinggi = int(input('Masukkan tinggi badan (cm) : '))
berat = int(input('Masukkan berat badan (kg) : '))
bmi = berat / (tinggi/100)**2

match pilihan:
    case 1:
        if bmi < 18:
            print(f'Anda tergolong Underweight dengan nilai BMI {bmi:.2f}')
        elif bmi >= 18 and bmi < 24:
            print(f'Anda tergolong Normal dengan nilai BMI {bmi:.2f}')
        elif bmi >= 24 and bmi < 27:
            print(f'Anda tergolong Overweight dengan nilai BMI {bmi:.2f}')
        elif bmi >= 27:
            print(f'Anda tergolong Obese dengan nilai BMI {bmi:.2f}')
    case 2:
        if bmi < 17:
            print(f'Anda tergolong Underweight dengan nilai BMI {bmi:.2f}')
        elif bmi >= 17 and bmi < 24:
            print(f'Anda tergolong Normal dengan nilai BMI {bmi:.2f}')
        elif bmi >= 24 and bmi < 28:
            print(f'Anda tergolong Overweight dengan nilai BMI {bmi:.2f}')
        elif bmi >= 28:
            print(f'Anda tergolong Obese dengan nilai BMI {bmi:.2f}')
    case _:
        print('Harap masukkan pilihan gender yang sesuai')