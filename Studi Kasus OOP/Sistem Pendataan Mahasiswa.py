class Mahasiswa:
    def __init__(self, nama, nim, prodi, ipk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.ipk = ipk

    def cek_status(self):
        if self.ipk >= 3:
            return "Lulus"
        else:
            return "Tidak Lulus"
    def tampilkan_info(self):
        status = self.cek_status()
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Prodi:", self.prodi)
        print("IPK:", self.ipk)
        print(status)
        print()

mhs1 = Mahasiswa("Jennie Kim", "250101001", "Sastra Mesin", 4)
mhs2 = Mahasiswa("Jungkook Jeon", "250101002", "Filsafat", 2.8)
mhs3 = Mahasiswa("Seungcheol Choi", "250101003", "Tadris IPA", 3)
mhs1.tampilkan_info()
mhs2.tampilkan_info()
mhs3.tampilkan_info()