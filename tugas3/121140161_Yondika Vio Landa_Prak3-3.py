# Nama : Yondika Vio Landa
# NIM : 121140161

class Hero:
    # Atribut public class, dapat diakses dari mana saja
    health = 100
    
    def __init__(self, nama, kekuatan, tipe_hero):
        # Atribut private, hanya dapat diakses dari dalam kelas ini
        self.__nama = nama
         # Atribut protected, hanya dapat diakses dari dalam kelas ini dan kelas turunan
        self._kekuatan = kekuatan
        # Atribut public, dapat diakses dari mana saja
        self.tipe_hero = tipe_hero
        
    def get_nama(self):
        # Fungsi getter, untuk mendapatkan nilai dari atribut private nama
        return self.__nama
    
    def __pilih_hero(self):
        # Fungsi private, hanya dapat diakses dari dalam kelas ini
        print("Nama Hero: " + self.__nama)
        print("Kekuatan : " + str(self._kekuatan))
        print("Darah : " + str(self.health))
        print("Role : " + self.tipe_hero)
        print("Siap memasuki pertandingan!")
        print()
        
    def _serang_lawan(self, lawan):
        # Fungsi protected, hanya dapat diakses dari dalam kelas ini dan kelas turunan
        print(self.__nama + " Menyerang " + lawan.__nama)
        print("Serangan " + self.__nama + " sebesar " + str(self._kekuatan))
        lawan.health = lawan.health - self._kekuatan
        if lawan.health > 0:
            print("Darah " + lawan.__nama + " sekarang tersisa " + str(lawan.health))
            print(lawan.__nama + " Melakukan serangan balik!")
            print()
            # pemanggilan fungsi protected
            lawan._serang_lawan(self)
        else:
            print(lawan.__nama + " berhasil diKalahkan! Darah " + lawan.__nama + " habis.")
            #pemanggilan fungsi public
            self.pemenang(self)
            exit()
            
    def pemenang(self, pemenang):
        # Fungsi public, dapat diakses dari mana saja
        print("Pemenangnya adalah " +  pemenang.__nama)
        if pemenang.health > 0:
            print("Darah tersisa : " + str(pemenang.health))
        else:
            print("Darah tersisa : 0")
    
# Membuat objek dari kelas Hero
hero1 = Hero("Balmond", 15, "Fighter")
hero2 = Hero("Nana", 20, "Mage")

# Pemanggilan fungsi private
hero1._Hero__pilih_hero()
# selama darah dari lawan belum habis, maka program terus berulang
while hero2.health > 0:
    # Pemanggilan fungsi protected
    hero1._serang_lawan(hero2)

        

