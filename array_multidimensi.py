# Kuota	Masa Berlaku	Harga
# 1GB	2 Hari	5000
# 2GB	5 Hari	10000
# 5GB	5 Hari	15000
# 7GB	7 Hari	20000
# 15GB	3 Hari	25000
# 3GB	30 Hari	20000
# 5GB	30 Hari	30000
# 12GB	30 Hari	50000
# 24GB	30 Hari	80000
# 35GB	30 Hari	100000
# 50GB	30 Hari	120000

# dibuat menggunakan array multidimensi
data = [
    ["1GB", "2 Hari", "5000"],
    ["2GB", "5 Hari", "10000"],
    ["5GB", "5 Hari", "15000"],
    ["7GB", "7 Hari", "20000"],
    ["15GB", "3 Hari", "25000"],
    ["3GB", "30 Hari", "20000"],
    ["5GB", "30 Hari", "30000"],
    ["12GB", "30 Hari", "50000"],
    ["24GB", "30 Hari", "80000"],
    ["35GB", "30 Hari", "100000"],
    ["50GB", "30 Hari", "120000"],
]

# fungsi untuk menampilkan data
def show_data():
    print("Kuota\tMasa Berlaku\tHarga")
    for i in data:
        print("\t".join(i))
    
# fungsi untuk menambah data
def add_data():
    kuota = input("Masukkan kuota: ")
    masa = input("Masukkan masa berlaku: ")
    harga = input("Masukkan harga: ")
    data.append([kuota, masa, harga])

# fungsi untuk menghapus data
def delete_data():
    show_data()
    index = int(input("Masukkan nomor data yang akan dihapus: "))
    del data[index-1]

# fungsi untuk mengubah data
def edit_data():
    show_data()
    index = int(input("Masukkan nomor data yang akan diubah: "))
    kuota = input("Masukkan kuota: ")
    masa = input("Masukkan masa berlaku: ")
    harga = input("Masukkan harga: ")
    data[index-1] = [kuota, masa, harga]

# fungsi untuk mencari data
def search_data():
    keyword = input("Masukkan keyword: ")
    for i in data:
        if keyword in i:
            print("\t".join(i))

# fungsi untuk menampilkan menu
def show_menu():
    print("Selamat datang")
    print("1. Tampilkan data")
    print("2. Tambah data")
    print("3. Hapus data")
    print("4. Ubah data")
    print("5. Cari data")
    print("6. Keluar")
    menu = input("Pilih menu : ")
    if menu == "1":
        show_data()
    elif menu == "2":
        add_data()
    elif menu == "3":
        delete_data()
    elif menu == "4":
        edit_data()
    elif menu == "5":
        search_data()
    elif menu == "6":
        exit()
    else:
        print("Menu tidak tersedia")

# fungsi utama
if __name__ == "__main__":
    while True:
        show_menu()
