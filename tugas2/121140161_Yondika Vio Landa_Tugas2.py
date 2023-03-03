class Mhs:
    def __init__(self,nama,nim,kelas_pbo,sks):
        self.nama = nama
        self.nim = nim
        self.kelas_pbo = kelas_pbo
        self.sks = sks
    
    def ambil_sks(self):
        print(str(self.nama) + " dengan NIM " + str(self.nim) + " dari kelas PBO " + str(self.kelas_pbo) + " mengambil " + str(self.sks) + " SKS.")
    
nama = str(input("Masukkan Nama: "))
nim = str(input("Masukkan NIM: "))
sks = str(input("Masukkan SKS: "))

saya = Mhs(nama, nim, "RB", sks )

saya.ambil_sks()