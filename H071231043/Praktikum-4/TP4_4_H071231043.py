def CatAndMouse(CatA, CatB, MouseC):
    a = abs(CatA - MouseC)
    b = abs(CatB - MouseC)

    if a > b:
        return "Cat B"
    elif a < b:
        return "Cat B"
    else:
        return "Mouse C"
    
#case1
print(CatAndMouse(CatA= 2, CatB= 1, MouseC= 4))
# print