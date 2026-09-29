# =====================================================================
# KASUS 03 - MULTIPLE INHERITANCE: Sistem Manajemen Pegawai
# Induk 1: Pegawai      (id_pegawai, nama)
# Induk 2: Gaji         (gaji)
# Induk 3: PegawaiProyek(nama_proyek)
# Anak   : ProjectManager mewarisi ketiga class induk
# =====================================================================
class Pegawai:
    def __init__(self, id_pegawai, nama, **kwargs):
        super().__init__(**kwargs)
        self.id_pegawai = id_pegawai
        self.nama = nama


class Gaji:
    def __init__(self, gaji, **kwargs):
        super().__init__(**kwargs)
        self.gaji = gaji

    def tampilkan_gaji(self):
        print(f"Gaji         : Rp{self.gaji:,.0f}".replace(",", "."))


class PegawaiProyek:
    def __init__(self, nama_proyek, **kwargs):
        super().__init__(**kwargs)
        self.nama_proyek = nama_proyek

    def tampilkan_proyek(self):
        print(f"Nama Proyek  : {self.nama_proyek}")


class ProjectManager(Pegawai, Gaji, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        super().__init__(
            id_pegawai=id_pegawai,
            nama=nama,
            gaji=gaji,
            nama_proyek=nama_proyek,
        )

    def tampilkan_data(self):
        print("[PROJECT MANAGER]")
        print(f"ID Pegawai   : {self.id_pegawai}")
        print(f"Nama         : {self.nama}")
        self.tampilkan_gaji()
        self.tampilkan_proyek()
        print("-" * 30)


def kasus_03():
    print("\n" + "=" * 40)
    print("KASUS 03 - SISTEM MANAJEMEN PEGAWAI")
    print("=" * 40)

    pm = ProjectManager("PM-006", "Jiwoo Kim", 50000000, "Host Live Aplikasi E-Commerce")
    pm.tampilkan_data()

    # Bukti pewarisan majemuk
    print("Urutan pewarisan (MRO):")
    print(" -> ".join(cls.__name__ for cls in ProjectManager.__mro__))
