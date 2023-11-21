class Bentuk:
    def __init__(self, nama):
        self.nama = nama

    def menghitung_luas(self):
        pass

class Bulat(Bentuk):
    def __init__(self, nama, radius):
        super().__init__(nama)
        self._radius = radius

    def menghitung_luas(self):
        return 3.14 * self._radius**2
    
    def get_radius(self):
        return self._radius
    
    def set_radius(self,radius):
        self._radius = radius

class SegiEmpat(Bentuk):
    def __init__(self, nama, panjang_sisi):
        super().__init__(nama)
        self._panjang_sisi = panjang_sisi

    def menghitung_luas(self):
        return self._panjang_sisi * self._panjang_sisi
    
    def get_radius(self):
        return self._panjang_sisi
    
    def set_panjang_sisi(self,panj_panjang_sisi):
        self._panjang_sisi = panj_panjang_sisi

bulat = Bulat("Lingkaran", 5)
# bulat.set_radius(6)
segi_empat = SegiEmpat("Persegi", 4)
# segi_empat.set_panjang_sisi(8)

bentuk = [bulat, segi_empat]
for i in bentuk:
    print(f"Nama: {i.nama}, Luas: {i.menghitung_luas()}")