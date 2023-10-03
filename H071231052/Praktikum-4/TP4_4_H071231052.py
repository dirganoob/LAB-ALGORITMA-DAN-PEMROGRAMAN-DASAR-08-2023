def mouseAndCat(catA, catB, mosC):
    jarakA = abs(catA - mosC)
    jarakB = abs(catB - mosC)
    
    if jarakA < jarakB:
        return "Cat A"
    elif jarakA > jarakB :
        return "Cat B"
    else:
        return "Mouse C"

A = int(input('Masukkan posisi Cat A : '))
B = int(input('Masukkan posisi Cat B : '))
C = int(input('Masukkan posisi Mouse C : '))

output = mouseAndCat(A, B, C)
print(f"-> {output}")