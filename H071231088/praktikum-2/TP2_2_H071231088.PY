x = input("masukkan input pertama : ")
if x not in ["vertebrado", "invertebrado"]:
    exit()

y = input("masukkan input kedua : " )
if y not in ["ave", "mamifero", "inseto", "anelideo"]:
    exit()

z = input("masukkan input ketiga : ")

match x, y, z :
    case "vertebrado", "ave,", "carnivoro":
        print("agula")
    case "vertebrado", "ave", "onivoro":
        print("ppmba")
    case "vertebrado", "mamivero", "onivoro":
        print("homem")
    case "vertebrado", "mamivero", "herbivoro":
        print("vaca")
    case "invertebrado", "inseto", "hematofago":
        print("pulga")
    case "invertebrado", "inseto", "herbivoro":
        print("lagarta")
    case "invertebrado", "anelideo", "hematofago":
        print("sanguessuga")
    case "invertebrado", "anelideo", "onivoro":
        print("minhoca")
    case _:
        print("invalid input")



# x = input("masukkan input pertama : ")
# if x not in ["vertebrado", "invertebrado"]:
#     exit()

