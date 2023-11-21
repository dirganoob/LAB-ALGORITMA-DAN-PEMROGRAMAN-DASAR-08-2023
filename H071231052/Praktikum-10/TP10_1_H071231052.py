import re
import os

class Detail:
    def __init__(self):
        self.nama = ""
        self.email = ""
        self.password = ""
        
def Menu():
    print(f"{'='*50}")
    print(f"Silahkan pilih opsi menu anda :")
    print(f"1. Detail Anda\n2. Ubah Nama \n3. Jumlah Data Pada File\n4. Save Data Pada File\n5. Buat Data Baru\n6. Keluar")
    
def Nama():
    nama = input("Silahkan Masukkan Nama Anda : ")
    pattern_nama = re.findall(r"[a-zA-Z0-9\s]*", nama)
    if pattern_nama:
        return nama
    else:
        print(f"{'='*50}\nFormat nama hanya berupa kombinasi huruf dan angka!\n{'='*50}")
        Nama()
        
def Email():
    email = input("Silahkan Masukkan Email Anda : ")
    pattern_email = re.findall(r"^[a-z]+[\d]{2,}@[a-z]+\.([a-z]*\.)?(com|co\.id|ac\.id)$", email)
    if pattern_email:
        return email
    else:
        print(f"{'='*50}\nEmail yang anda masukkan salah!\n{'='*50}")
        Email()
def Password():
    password = input("Silahkan Masukkan Password Anda : ")
    pattern_password = re.findall(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9]{8,20}", password)
    if pattern_password:
        return password
    elif len(password) < 8 or len(password) > 20:
        print(f"{'='*50}\nPassword Harus Memiliki Panjang 8-20\n{'='*50}")
        Password()
    else:
        print(f"{'='*50}\nPassword yang anda masukkan terlalu lemah!\nGunakan minimal 1 huruf kapital, huruf kecil, dan angka\n{'='*50}")
        Password()

akun = Detail()
while True:
    Menu()
    pilihan = int(input("Silahkan Pilih Opsi Anda : "))
    match pilihan:
        case 1:
            if akun.nama is "" and akun.email is "" and akun.password is "":
                print(f"{'='*50}\nData Saat Ini Kosong!")
            else:
                print(f"{'='*50}\nData anda adalah :\nNama : {akun.nama}\nEmail : {akun.email}\nPassword : {akun.password[0]}{(len(akun.password)-2)*'*'}{akun.password[-1]}")
        case 2:
            if akun.nama is "":
                print(f"{'='*50}\nData Saat Ini Kosong!")
            else:
                akun.nama = input(f"{'='*50}\nSilahkan Input Nama Baru : ")
        case 3:
            print(f"{'='*50}")
            nama_file = input("Silahkan Masukkan Nama File : ") + ".txt"
            if not os.path.exists(nama_file):
                print(f"{'='*50}")
                print(f"Tidak Terdapat File Dengan Nama {nama_file[:-4]}")
                print("Jumlah data pada file berjumlah 0")
            else:
                with open(nama_file,"r") as data:
                    pattern_jumlah = re.findall(r"Nama\t\t: ", data.read())
                    print(f"{'='*50}")
                    print("File Ditemukan")
                    print(f"Jumlah data pada file berjumlah {len(pattern_jumlah)}")
                     
                
        case 4:
            if akun.nama is "" and akun.email is "" and akun.password is "":
                print(f"{'='*50}\nData Saat Ini Kosong, Tidak Dapat Save!")
            else:
                print(f"{'='*50}")
                nama_file = input("Silahkan Masukkan Nama File : ") + ".txt"
                if not os.path.exists(nama_file):
                    with open(nama_file,"a") as file:
                        file.write(f"+{'='*99}\n")
                        file.write(f"|Data yang tersimpan\n")
                        file.write(f"+{'='*99}\n")
                with open(nama_file,"a") as file:
                    file.write(f"Nama\t\t: {akun.nama}\n")
                    file.write(f"Email\t\t: {akun.email}\n")
                    file.write(f"Password\t: {akun.password}\n")
                    file.write(f"+{'='*99}\n")
                print("Berhasil!")
                akun = Detail()
        case 5:
            print(f"{'='*50}")
            akun.nama = Nama()
            akun.email = Email()
            akun.password = Password()
        case 6:
            print(f"{'='*50}\nSee You Next Time!!")
            break
        case _:
            print(f"Hayya lu olang jangan asal pencet oo!")
            break