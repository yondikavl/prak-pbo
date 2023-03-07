# Nama : Yondika Vio Landa
# NIM : 121140161

class AkunBank:
    # Ini adalah atribut kelas yang berisi data-data pelanggan, berupa list kosong
    list_pelanggan = []
    
    # Ini adalah konstruktor atau atribut instance yang akan dijalankan setiap kali objek dibuat. 
    def __init__(self,no_pelanggan,nama_pelanggan,jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        # no pelanggan dari tiap objek yang dibuat akan masuk ke list list_pelanggan
        AkunBank.list_pelanggan.append(self.__no_pelanggan)
    # Ini adalah metode getter yang berfungsi untuk mengembalikan nilai dari atribut no_pelanggan
    def get_no_pelanggan(self):
        return self.__no_pelanggan
    # Ini adalah metode getter yang berfungsi untuk mengembalikan nilai dari atribut nama_pelanggan
    def get_nama_pelanggan(self):
        return self.__nama_pelanggan
    # Ini adalah metode getter yang berfungsi untuk mengembalikan nilai dari atribut jumlah_saldo
    def get_jumlah_saldo(self):
        return self.__jumlah_saldo
    # Ini adalah metode yang berfungsi untuk menampilkan menu utama dan mengambil pilihan pengguna. 
    def lihat_menu(self):
        print("\nSelamat datang di Bank Jago")
        print("Halo " + str(self.__nama_pelanggan) + ", ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")
        pilihan_menu = int(input("Masukkan nomor input: "))
        
        if pilihan_menu == 1: # Jika pengguna memilih opsi 1, maka akan memanggil metode lihat_saldo().
            self.lihat_saldo()
        elif pilihan_menu == 2: # Jika pengguna memilih opsi 2,  maka akan memanggil metode tarik_tunai().
            self.tarik_tunai()
        elif pilihan_menu == 3: # Jika pengguna memilih opsi 3, maka akan memanggil metode transfer().
            self.transfer()
        else: # Jika pengguna memilih opsi 4, maka program akan keluar.
            exit()
    # Ini adalah metode yang berfungsi untuk menampilkan jumlah saldo pengguna.
    def lihat_saldo(self):
        print(str(self.__nama_pelanggan) + " memiliki saldo Rp " + str(self.__jumlah_saldo))
    # Ini adalah metode yang berfungsi untuk menarik tunai dari saldo pengguna.
    def tarik_tunai(self):
        # Metode ini akan meminta pengguna untuk memasukkan nominal yang ingin ditarik,
        saldo_ditarik = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        # dan akan mengecek apakah saldo mencukupi. Jika mencukupi, saldo akan dikurangi
        while saldo_ditarik > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
            saldo_ditarik = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
            
        self.__jumlah_saldo = self.__jumlah_saldo - saldo_ditarik
        print("Saldo berhasil ditarik!")
    # Ini adalah metode yang berfungsi untuk mengirim saldo dari saldo pengguna ke pengguna lain
    def transfer(self):
        # Metode ini akan meminta pengguna untuk memasukkan nominal yang ingin dikirim dan nomor rekening tujuan
        saldo_kirim = int(input("Masukkan nominal yang ingin ditransfer: "))
        no_rek_tujuan = int(input("Masukkan no rekening tujuan: "))
        # dan akan mengecek apakah no rekening yang dimasukkan sesuai/ada atau tidak.
        # Jika sesuai, saldo akan dikirim dan saldo pengguna akan dikurangi 
        if no_rek_tujuan in AkunBank.list_pelanggan:
            self.__jumlah_saldo = self.__jumlah_saldo - saldo_kirim
            print("Transfer " + str(saldo_kirim) + " ke " + str(no_rek_tujuan) + " sukses!")
        else:
            print("No rekening tujuan tidak dikenali! Kembali ke menu utama ...")        
    
# daftar objek AkunBank
Akun1 = AkunBank(1234, "Yondika Vio Landa", 500000)
Akun2 = AkunBank(2345, "Ukraina", 666666)
Akun3 = AkunBank(3456, "Elon Musk", 999999)

# program akan menjalankan fungsi lihat_menu dari objek Akun1 secara terus-menerus selama variabel keluar bernilai False. 
# Hal ini akan terus berlangsung sampai adanya perintah untuk keluar dari program.
keluar = False

while keluar == False:
    Akun1.lihat_menu()

    
    
    