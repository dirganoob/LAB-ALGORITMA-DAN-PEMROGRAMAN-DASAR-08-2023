import re

def string_valid(string):
    pattern = r"^[A-Za-z2468]{40}[13579\s]{5}$"
    return re.search(pattern,string)

string = input("Masukkan String : ")
if string_valid(string):
    print(True)
else:
    print(False)