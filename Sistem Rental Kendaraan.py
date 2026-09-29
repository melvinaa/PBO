# =====================================================================
# KASUS 02 - INHERITANCE: Sistem Rental Kendaraan
# Induk    : Kendaraan (nama, merk, tahun, kecepatan)
# Turunan 1: Mobil (+ jumlah_kursi)
# Turunan 2: Motor (+ tipe_motor)
# =====================================================================
class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def tampilkan_info(self):
        print(f"Nama      : {self.nama}")
        print(f"Merk      : {self.merk}")
        print(f"Tahun     : {self.tahun}")
        print(f"Kecepatan : {self.kecepatan} km/jam")


class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def tampilkan_info(self):
        print("[MOBIL]")
        super().tampilkan_info()
        print(f"Jml Kursi : {self.jumlah_kursi}")
        print("-" * 30)


class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def tampilkan_info(self):
        print("[MOTOR]")
        super().tampilkan_info()
        print(f"Tipe      : {self.tipe_motor}")
        print("-" * 30)


def kasus_02():
    print("\n" + "=" * 40)
    print("KASUS 02 - SISTEM RENTAL KENDARAAN")
    print("=" * 40)

    mobil = Mobil("GLS 450", "Mercedes-Benz", 2026, 250, 7)
    motor = Motor("Sprint Tech 180", "Vespa", 2026, 120, "Matic")

    mobil.tampilkan_info()
    motor.tampilkan_info()