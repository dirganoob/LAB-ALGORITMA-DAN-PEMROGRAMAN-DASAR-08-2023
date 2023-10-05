def CatAndMouse(CatA, CatB, MouseC):
    a = abs(CatA - MouseC)
    b = abs(CatB - MouseC)
    
    if a < b:
        return "Cat A"
    elif b < a:
        return "Cat B"
    else:
        return "Mouse C"
    
# case1
result1 = CatAndMouse(CatA = 16, CatB = 24, MouseC = 15)
print(result1)

# case2
result2 = CatAndMouse(CatA = 20, CatB = 10, MouseC = 15)
print(result2)