# Nama : Yondika Vio Landa
# NIM : 121140161

class Karyawan:
    # Atribut public, dapat diakses dari mana saja
    salary = 0

    def __init__(self, nama, umur):
        # Atribut private, hanya dapat diakses dari dalam kelas ini
        self.__nama = nama
        # Atribut protected, hanya dapat diakses dari dalam kelas ini dan kelas turunan
        self._umur = umur

    def say_hello(self):
        # Fungsi public, dapat diakses dari mana saja
        print("Halo, nama saya " + self.__nama + " dan umur saya " + str(self._umur) + " tahun.")

    def get_salary(self):
        # Fungsi public, dapat diakses dari mana saja
        return self.salary

# Membuat kelas turunan dari kelas Karyawan
class Manajer(Karyawan):
    def __init__(self, nama, umur, departemen):
        # Memanggil konstruktor dari kelas induk (Karyawan)
        super().__init__(nama, umur)
        # Atribut public, dapat diakses dari mana saja
        self.departemen = departemen

    def say_hello(self):
        # Memanggil fungsi say_hello dari kelas induk (Karyawan) dan menambahkan pesan tambahan
        super().say_hello()
        print("Saya bekerja di departemen " +  self.departemen )

# Membuat objek dari kelas Karyawan
Karyawan1 = Karyawan("Eko", 30)

# Mengakses atribut dan fungsi dengan berbagai tingkat aksesibilitas
Karyawan1.say_hello()  # Output: Halo, nama saya Eko dan umur saya 30 tahun.
Karyawan1.salary = 5000
print(Karyawan1.get_salary())  # Output: 5000
Karyawan1._umur = 31
print(Karyawan1._umur)  # Output: 31
Karyawan1.__nama = "Jane"  # Nama tidak akan berubah karena atribut ini bersifat private dan tidak dapat diakses dari luar kelas
Karyawan1.say_hello() # kita coba buktikan, nama akan tetap Eko

# Membuat objek dari kelas Manajer
Manajer1 = Manajer("Agus", 35, "Marketing")

# Mengakses atribut dan fungsi dengan berbagai tingkat aksesibilitas dari objek kelas Manajer
Manajer1.say_hello()  # Output: Halo, nama saya Agus dan umur saya 35 tahun.
Manajer1.salary = 7000
print(Manajer1.get_salary())  # Output: 7000
Manajer1._umur = 36
print(Manajer1._umur)  # Output: 36
