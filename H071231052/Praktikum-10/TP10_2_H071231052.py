from abc import ABC, abstractmethod

class Brand(ABC):
    def __init__(self):
        self.__produk = None
        self.__brand = None
    @abstractmethod
    def iklan(self):
        pass

    @property
    def info(self):
        print(f"merupakan produk {self.__produk} dengan brand {self.__brand}")

    @property
    def produk(self):
        pass
    @produk.getter
    def produk(self):
        return self.__produk
    @produk.setter
    def produk(self, input):
        self.__produk = input
    
    @property
    def brand(self):
        pass
    @brand.getter
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, input):
        self.__brand = input
    
class Nike(Brand):
    def __init__(self):
        self.produk = "Sepatu"
        self.brand = "NIKE"

    def iklan(self):
        print("Just Do it")

class LeMinerale(Brand):
    def __init__(self):
        self.produk = "Minuman"
        self.brand = "LEMINERALE"

    def iklan(self):
        print("Ada manis-manisnya!")

class CapKakiTiga(Brand):
    def __init__(self):
        self.produk = "Minuman"
        self.brand = "CapKakiTiga"

    def iklan(self):
        print("Yang Ada BADAKNYA!!!")

airMinum = LeMinerale()
sepatu = Nike()

sepatu.iklan()
airMinum.iklan()
print("info dari si sepatu :")
sepatu.info
print(airMinum.__dict__)