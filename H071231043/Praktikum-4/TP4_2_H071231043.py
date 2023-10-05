def palindrom(kata: str):
    kata = kata.lower().replace(" ", "")

    if kata == kata [::-1]: 
        return "Palindrom"
    else:
        return "Bukan Palindrom"
    
kata = str("Ubi Ibu")
print(palindrom(kata))