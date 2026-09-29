# =====================================================================
# KASUS 01 - CLASS & OBJECT: Sistem Pendataan Mahasiswa
# Atribut : nama, nim, jurusan (+ nilai untuk logika kelulusan)
# Logika  : cek_status() -> lulus jika nilai >= 75
# =====================================================================
class Mahasiswa:
    def __init__(self, nama, nim, jurusan, nilai):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = nilai

    def cek_status(self):
        return "LULUS" if self.nilai >= 75 else "TIDAK LULUS"

    def tampilkan_profil(self):
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Nilai   : {self.nilai}")
        print(f"Status  : {self.cek_status()}")
        print("-" * 30)


def kasus_01():
    print("=" * 40)
    print("KASUS 01 - SISTEM PENDATAAN MAHASISWA")
    print("=" * 40)

    # Minimal 3 objek mahasiswa
    daftar_mahasiswa = [
        Mahasiswa("Jennie Kim", "250101001", "Sastra Mesin", 83),
        Mahasiswa("Jungkook Jeon", "250101002", "Filsafat", 70),
        Mahasiswa("Seungcheol Choi", "250101003", "Tadris IPA", 75),
    ]

    # Cetak profil seluruh data
    for mhs in daftar_mahasiswa:
        mhs.tampilkan_profil()