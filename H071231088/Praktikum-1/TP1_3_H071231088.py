print("program menerima inputan a, b, dan c yang bertipe data numerik dengan a != 0")

a = float(input("masukkan a : "))# a !=0
if a == 0:
    print("a tidak boleh sama dengan 0")
    exit()
else:

    b = float(input("masukkan b : "))
    c = float(input("masukkan c : "))

D = (b**2) - (4*a*c)

x1 = (-b + (D ** 0.5)) / (2*a)  
x2 = (-b - (D ** 0.5)) / (2*a)
print(f"nilai X1 = {x1:.2f}")
print(f"nilai X2 = {x2:.2f}")
