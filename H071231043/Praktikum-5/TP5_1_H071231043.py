s1 = input("s1 = ").replace(" ", "")
s2 = input("s2 = ").replace(" ", "")[::-1]
s3 = ""
m = min(len(s1), len(s2))

for i in range(m):
    campuran = s1[i] + s2[i]
    s3 += campuran

s3 += s1[m:] + s2[m:]
print(f'hasil = "{s3}"')




















# naura

# def campuran(s1, s2):
#     s3 = ""
#     string1 = len(s1)
#     string2 = len(s2)
#     campuran = max(string1, string2)
   
#     for i in range(campuran):
#         if i < string1 and i < string2 :
#             s3 += s1[i] + s2[-(i+1)]
#             i += 1
#     s3 += s1[i:]+ s2[i:]
#     return s3

# a = input()
# b = input()
# hasil = campuran(a, b)
# print(hasil)       


# sabil

# def campuran(s1, s2):
#     s2 = ''.join(reversed(s2))
#     m = ""

#     for i in range(len(s1)):
#         m = m + s1[i] + s2[i]
#     return m

# s1 = input("Masukkan String Pertama : ")
# s2 = input("Masukkan String Kedua : ")
# print(campuran(s1, s2))


# padiley

# s1 = input("")
# s2 = input("")
# def karakter(s1, s2):
#     panjang = min(len(s1), len(s2))
#     s3 = ''.join([s1[i] + s2[-(i+1)] for i in range(panjang)])
#     s3 += s1[panjang:] + s2[panjang:]
#     return s3
# s3 = karakter(s1, s2)
# print(s3)

# eky

# input1 = input("Masukkan kata1: ")
# input2 = input("Masukkan kata2: ")
# hasil = ""
# i = 0

# while i < len(input1) and i < len(input2):
#     hasil += input1[i] + input2[-(i+1)]
#     i += 1
# hasil += input1[1:] + input2[1:]
# print(hasil)

# cholyn
