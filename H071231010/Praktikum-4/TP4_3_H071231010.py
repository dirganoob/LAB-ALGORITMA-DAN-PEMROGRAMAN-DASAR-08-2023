def maksimum(*args):
    if len(args) == 0:
        raise ValueError("Daftar angka kosong")
    
    max_num = args[0]
    for n in args:
        if n < max_num:
            max_num = n
    
    return max_num

# Test Case 1
print(maksimum(1,2,4,6,9,3,1,9,10))  


