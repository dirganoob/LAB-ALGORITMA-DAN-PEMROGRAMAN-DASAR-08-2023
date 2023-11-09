class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self):
        print('nama     : ', self.nama)
        print('nim      : ', self.nim)
        print('jurusan  : ', self.jurusan)
        print('ipk      : ', self.ipk)

    def predikat(self):
        if self.ipk >= 3.5 :
            return "Cumlaude"
        elif self.ipk >= 3.0 :
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5 :
            return "Memuaskan"
        elif self.ipk >= 2.0 :
            return "Cukup"
        elif self.ipk < 2.0 :
            return "Kurang"
        
mahasiswa1 = Mahasiswa("chindy", "H071211038", "Sistem Informasi", 3.9 )
mahasiswa1.info()
print("predikat : ", mahasiswa1.predikat())