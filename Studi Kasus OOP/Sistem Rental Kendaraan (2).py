class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def tampilkan_data(self):
        print("Nama       :", self.nama)
        print("Merk       :", self.merk)
        print("Tahun      :", self.tahun)
        print("Kecepatan  :", self.kecepatan, "km/jam")


class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Jumlah Kursi :", self.jumlah_kursi)


class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Tipe Motor :", self.tipe_motor)


# 3 Objek Mobil
mobil1 = Mobil("Aventador SVJ", "Lamborghini", 2023, 350, 2)
mobil2 = Mobil("Chiron", "Bugatti", 2024, 420, 2)
mobil3 = Mobil("G 63 AMG", "Mercedes-Benz", 2024, 240, 5)


# 3 Objek Motor
motor1 = Motor("Panigale V4 R", "Ducati", 2024, 300, "Sport")
motor2 = Motor("Ninja H2R", "Kawasaki", 2023, 400, "Supercharged")
motor3 = Motor("Gold Wing", "Honda", 2024, 180, "Touring")


print("DATA MOBIL 1")
mobil1.tampilkan_data()
print()

print("DATA MOBIL 2")
mobil2.tampilkan_data()
print()

print("DATA MOBIL 3")
mobil3.tampilkan_data()
print()

print("DATA MOTOR 1")
motor1.tampilkan_data()
print()

print("DATA MOTOR 2")
motor2.tampilkan_data()
print()

print("DATA MOTOR 3")
motor3.tampilkan_data()
print()