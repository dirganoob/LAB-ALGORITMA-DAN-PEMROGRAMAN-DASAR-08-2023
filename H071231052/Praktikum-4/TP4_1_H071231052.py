def kombinasi(kata, suku=0):
    try:
        print(kata, end=" | ")
        kata = kata[-1] + kata[:-1]
        suku +=1
        if suku < len(kata):
            kombinasi(kata, suku)
    except TypeError as err:
        print(err)

target = input("Masukkan kata kombinasi : ")
kombinasi(target)