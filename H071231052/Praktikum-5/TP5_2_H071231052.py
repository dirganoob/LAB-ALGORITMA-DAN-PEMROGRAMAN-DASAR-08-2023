var = input("Masukkan kata : ")
mid = len(var)//2

if len(var)%2 != 0:
    print(var[0]+var[mid]+var[-1])
else:
    print(var[0]+var[mid-1], var[mid]+var[-1])
