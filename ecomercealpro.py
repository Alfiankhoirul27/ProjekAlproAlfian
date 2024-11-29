import getpass

# Data penyimpanan sementara
pengguna = {}  # {"nama_pengguna": {"kata_sandi": "kata_sandi", "keranjang": []}}
penjual = {"nama_pengguna": "seller", "kata_sandi": "seller123"}  # Akun penjual tunggal
produk = []  # [{"id": 1, "nama": "Produk", "harga": 1000, "stok": 10}]

# Fungsi Registrasi Pengguna
def daftar_pengguna():
    print("\n--- Daftar Pengguna ---")
    nama_pengguna = input("Masukkan nama pengguna: ")
    if nama_pengguna in pengguna:
        print("Nama pengguna sudah terdaftar.")
        return
    kata_sandi = getpass.getpass("Masukkan kata sandi: ")
    pengguna[nama_pengguna] = {"kata_sandi": kata_sandi, "keranjang": []}
    print("Registrasi berhasil!")

# Fungsi Login
def masuk(peran):
    print(f"\n--- Masuk sebagai {peran.title()} ---")
    nama_pengguna = input("Masukkan nama pengguna: ")
    kata_sandi = getpass.getpass("Masukkan kata sandi: ")
    if peran == "pengguna" and nama_pengguna in pengguna and pengguna[nama_pengguna]["kata_sandi"] == kata_sandi:
        print("Masuk berhasil!")
        return nama_pengguna
    elif peran == "penjual" and nama_pengguna == penjual["nama_pengguna"] and kata_sandi == penjual["kata_sandi"]:
        print("Masuk berhasil!")
        return nama_pengguna
    print("Nama pengguna atau kata sandi salah.")
    return None

# Fungsi Pengelolaan Produk oleh Penjual
def tambah_produk():
    print("\n--- Tambah Produk ---")
    nama = input("Masukkan nama produk: ")
    harga = int(input("Masukkan harga produk: "))
    stok = int(input("Masukkan stok produk: "))
    id_produk = len(produk) + 1
    produk.append({"id": id_produk, "nama": nama, "harga": harga, "stok": stok})
    print("Produk berhasil ditambahkan!")

def ubah_produk():
    lihat_produk()
    id_produk = int(input("Masukkan ID produk yang ingin diubah: "))
    for item in produk:
        if item["id"] == id_produk:
            print(f"Produk terpilih: {item['nama']}")
            item["nama"] = input("Masukkan nama baru produk: ")
            item["harga"] = int(input("Masukkan harga baru produk: "))
            item["stok"] = int(input("Masukkan stok baru produk: "))
            print("Produk berhasil diubah!")
            return
    print("Produk tidak ditemukan.")

def hapus_produk():
    lihat_produk()
    id_produk = int(input("Masukkan ID produk yang ingin dihapus: "))
    for item in produk:
        if item["id"] == id_produk:
            produk.remove(item)
            print("Produk berhasil dihapus!")
            return
    print("Produk tidak ditemukan.")

# Fungsi Lihat Produk
def lihat_produk():
    print("\n--- Daftar Produk ---")
    if not produk:
        print("Belum ada produk tersedia.")
        return
    for item in produk:
        print(f"ID: {item['id']}, Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")

# Fungsi Pengguna Menambahkan ke Keranjang
def tambah_ke_keranjang(pengguna_aktif):
    lihat_produk()
    id_produk = int(input("Masukkan ID produk yang ingin ditambahkan ke keranjang: "))
    jumlah = int(input("Masukkan jumlah: "))
    for item in produk:
        if item["id"] == id_produk and item["stok"] >= jumlah:
            pengguna[pengguna_aktif]["keranjang"].append((id_produk, jumlah))
            print("Produk berhasil ditambahkan ke keranjang!")
            return
    print("Produk tidak ditemukan atau stok tidak mencukupi.")

# Fungsi Checkout
def checkout(pengguna_aktif):
    print("\n--- Checkout ---")
    keranjang = pengguna[pengguna_aktif]["keranjang"]
    if not keranjang:
        print("Keranjang kosong.")
        return
    total = 0
    for item in keranjang:
        produk_terpilih = next((p for p in produk if p["id"] == item[0]), None)
        if produk_terpilih:
            print(f"{produk_terpilih['nama']} x {item[1]} @ {produk_terpilih['harga']} = {produk_terpilih['harga'] * item[1]}")
            total += produk_terpilih["harga"] * item[1]
            produk_terpilih["stok"] -= item[1]
    print(f"Total belanja: {total}")
    pengguna[pengguna_aktif]["keranjang"] = []
    print("Checkout berhasil!")

# Menu Utama
def utama():
    while True:
        print("\n--- E-Commerce CLI ---")
        print("1. Daftar Pengguna")
        print("2. Masuk sebagai Pengguna")
        print("3. Masuk sebagai Penjual")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            daftar_pengguna()
        elif pilihan == "2":
            pengguna_aktif = masuk("pengguna")
            if pengguna_aktif:
                while True:
                    print("\n--- Menu Pengguna ---")
                    print("1. Lihat Produk")
                    print("2. Tambah ke Keranjang")
                    print("3. Checkout")
                    print("4. Keluar")
                    pilihan_pengguna = input("Pilih menu: ")
                    if pilihan_pengguna == "1":
                        lihat_produk()
                    elif pilihan_pengguna == "2":
                        tambah_ke_keranjang(pengguna_aktif)
                    elif pilihan_pengguna == "3":
                        checkout(pengguna_aktif)
                    elif pilihan_pengguna == "4":
                        break
                    else:
                        print("Pilihan tidak valid.")
        elif pilihan == "3":
            penjual_aktif = masuk("penjual")
            if penjual_aktif:
                while True:
                    print("\n--- Menu Penjual ---")
                    print("1. Tambah Produk")
                    print("2. Ubah Produk")
                    print("3. Hapus Produk")
                    print("4. Lihat Produk")
                    print("5. Keluar")
                    pilihan_penjual = input("Pilih menu: ")
                    if pilihan_penjual == "1":
                        tambah_produk()
                    elif pilihan_penjual == "2":
                        ubah_produk()
                    elif pilihan_penjual == "3":
                        hapus_produk()
                    elif pilihan_penjual == "4":
                        lihat_produk()
                    elif pilihan_penjual == "5":
                        break
                    else:
                        print("Pilihan tidak valid.")
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")

# Jalankan program
utama()
