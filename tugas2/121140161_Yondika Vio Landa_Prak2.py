# Nama : Yondika Vio Landa
# NIM : 121140161
# RB

# Kelas Mahasiswa
class Mhs:
    # atribut kelas "sks", untuk awal sks masih kosong karena belum ada mata kuliah yang diambil
    sks = 0 
    
    def __init__(self, nama, nim, kelas_pbo, ip):
    # menginisialisasi atribut objek "nama", "nim", "kelas_pbo", dan "ip" dari kelas Mahasiswa
        self.nama = nama
        self.nim = nim
        self.kelas_pbo = kelas_pbo
        # atribut ip harus diubah menjadi float agar dapat digunakan untuk komparasi
        self.ip = float(ip)

    def isi_krs(self):
        # menampilkan informasi nama, nim, dan jumlah sks yang diambil
        print(str(self.nama) + " dengan NIM " + str(self.nim) + " mengambil " + str(self.sks) + " SKS.\n")

    def tambah_sks_matkul(self, sks):
        # melakukan penambahan sks pada objek Mahasiswa
        if self.ip >= 3:
            # Jika IP Mahasiswa >= 3, maksimum SKS yang bisa diambil adalah 24
            if self.sks + sks <= 24:
                self.sks += sks
                print("Mata kuliah berhasil ditambahkan!")
            else:
                print("GAGAL MENAMBAHKAN, Jumlah SKS tidak mencukupi!")
        elif self.ip >= 2.75:
            # Jika IP Mahasiswa >= 2.75 dan < 3, maksimum SKS yang bisa diambil adalah 22
            if self.sks + sks <= 22:
                self.sks += sks
                print("Mata kuliah berhasil ditambahkan!")
            else:
                print("GAGAL MENAMBAHKAN, Jumlah SKS tidak mencukupi!")
        else:
            # Jika IP Mahasiswa < 2.75, maksimum SKS yang bisa diambil adalah 20
            if self.sks + sks <= 20:
                self.sks += sks
                print("Mata kuliah berhasil ditambahkan!")
            else:
                print("GAGAL MENAMBAHKAN, Jumlah SKS tidak mencukupi!")

    def cek_kelas_pbo(self):
        # menampilkan informasi kelas PBO yang diambil oleh objek Mahasiswa
        print("Kelas PBO yang diambil : " + str(self.kelas_pbo))

    
# nama = input("Masukkan Nama: ")
# nim = input("Masukkan NIM: ")
# ip = input("Masukkan IP: ")
# saya = Mhs(nama, nim, "RB", ip)

# menginisialisasi objek Mahasiswa dengan nama "Yondika Vio Landa", NIM "121140161", kelas PBO "RB", dan IP 3.5
saya = Mhs("Yondika Vio Landa", 121140161, "RB", 3.5)

# menampilkan informasi nama, nim, dan jumlah sks yang diambil oleh objek Mahasiswa
saya.isi_krs()
# menampilkan informasi kelas PBO yang diambil oleh objek Mahasiswa
saya.cek_kelas_pbo()
# menambahkan 4 sks mata kuliah
saya.tambah_sks_matkul(4)
saya.isi_krs()

saya.tambah_sks_matkul(3)
saya.isi_krs()

saya.tambah_sks_matkul(3)
saya.isi_krs()

saya.tambah_sks_matkul(3)
saya.isi_krs()

saya.tambah_sks_matkul(3)
saya.isi_krs()

saya.tambah_sks_matkul(2)
saya.isi_krs()

saya.tambah_sks_matkul(2)
saya.isi_krs()

saya.tambah_sks_matkul(2)
saya.isi_krs()

saya.tambah_sks_matkul(4)
saya.isi_krs()