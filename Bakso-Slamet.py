# Clean Console
import datetime
import os
import time
os.system("cls")

# Date and time
now = datetime.datetime.now()

# Bakso Slamet cabang Californiaaaaa
total = 0
pesanan = []
nama = ""
jumlahPesananBakso = 0
jumlahPesananMieAyam = 0
jumlahPesananTehManis = 0
jumlahPesananAqua = 0
diskonpersen = ""
sblmdiskon = 0
uang = 0
kembalian = 0
nomerMeja = 0

# Awal dari segala awal


def awal():
    global nama
    print("=" * 28)
    print("\tBakso Slamet\t")
    print("=" * 28, "\n")
    # Welcome
    print("Hai, Selamat Datang Di Bakso Slamet")
    print("Boleh saya tau siapa nama mu?")
    nama = input("Nama Pembeli : ")
    os.system("cls")
    print("mau pesan apa hari ini", nama, "?", "\n")

# Menu


def daftarMenu():
    global total, pesanan, jumlahPesananBakso, jumlahPesananMieAyam, jumlahPesananTehManis, jumlahPesananAqua, sblmdiskon
    print("========== Menu ==========")
    print("1. Bakso\t\tRp.8000")
    print("2. Mie Ayam\t\tRp.15000")
    print("3. Teh Manis\t\tRp.3000")
    print("4. Aqua\t\t\tRp.500")
    print("========== Menu ==========", "\n")
    pilih = int(input("Masukan pesanan [1/2/3/4] : "))
    if pilih == 1:
        jumlah = int(input("Masukan jumlah pembelian : "))
        harga1 = jumlah*8000
        total = total + harga1
        jumlahPesananBakso += jumlah
        pesanan += ["Bakso"]
        sblmdiskon += harga1
        print("Total pesanan : Rp.", total)
        fgstambah()
    elif pilih == 2:
        jumlah = int(input("Masukan jumlah pembelian : "))
        harga2 = jumlah*15000
        total = total + harga2
        jumlahPesananMieAyam += jumlah
        pesanan += ["MieAyam"]
        print("Total pesanan : Rp.", total)
        fgstambah()
    elif pilih == 3:
        jumlah = int(input("Masukan jumlah pembelian : "))
        harga3 = jumlah*3000
        total = total + harga3
        jumlahPesananTehManis += jumlah
        pesanan += ["TehManis"]
        print("Total pesanan : Rp.", total)
        fgstambah()
    elif pilih == 4:
        jumlah = int(input("Masukan jumlah pembelian : "))
        harga4 = jumlah*500
        total = total + harga4
        jumlahPesananAqua += jumlah
        pesanan += ["Aqua"]
        print("Total pesanan : Rp.", total)
        fgstambah()
    else:
        print("Menu tidak ada\n")
        daftarMenu()

# Tambah Pesanan


def fgstambah():
    global total
    print("\n-------------------------------")
    tambah = input("Ingin tambah pesanan? [y/n] : ")
    print("-------------------------------\n")
    if tambah == "y":
        daftarMenu()
    elif tambah == "n":
        print("Total pesanan : Rp.", total)
    else:
        print("Invalid kode bro")
        fgstambah()

# Kode kupon *Important feature


def kodeDiskon():
    global diskonpersen, total
    kode = input("Apakah anda punya Kode diskon? [y/n] : ")
    if kode == "y":
        kupon = input("\nMasukan kode diskon : ")
        if kupon == "diqu" or kupon == "moddy" or kupon == "drxx":
            diskon = total * (10/100)
            total = total - diskon
            diskonpersen += "10%"
            print("Dapet diskon cuy 10%")
            print("Final price anda : Rp.", total)
            akhir()
        elif kupon == "ryo":
            diskon = total * (40/100)
            total = total - diskon
            diskonpersen += "50%"
            print("Dapet diskon cuy 40%")
            print("Final price anda : Rp.", total)
            akhir()
        elif kupon == "ryzenzen":
            diskon = total * (20/100)
            total = total - diskon
            diskonpersen += "20%"
            print("Dapet diskon cuy 20%")
            print("Final price anda : Rp.", total)
            akhir()
        else:
            print("Invalid kode kupon cuy")
            kodeDiskon()
    elif kode == "n":
        akhir()
    else:
        print("Invalid kode bro")
        kodeDiskon()

# Dont forget to pay!!!!


def akhir():
    global total, uang, kembalian, uangKurang
    uang = float(input("Masukan uang anda : Rp."))
    print("\n-------------------------------")
    if uang > total:
        kembalian = uang - total
        antrian()
    elif uang < total:
        uangKurang = total - uang
        print("uwang lu kurang jir")
        akhir()
    else:
        antrian()

# Nomer Meja


def antrian():
    global nomerMeja
    print("Ambil nomer meja")
    nomerMeja = int(input("Masukan nomer meja : "))
    struk()


# clear
os.system("cls")

# Sturk
hargabakso = 8000
hargamieayam = 15000
hargatehmanis = 3000
hargaaqua = 500


def struk():
    os.system("cls")
    time.sleep(1)
    global nama, jumlahPesananBakso, jumlahPesananMieAyam, jumlahPesananTehManis, jumlahPesananAqua, pesanan, harga, diskonpersen, uang, kembalian, nomerMeja
    pesanan = set(pesanan)
    print("=" * 40)
    print("              Baskso Slamet")
    print("            Cabang California")
    print("=" * 40)
    print(now.strftime("%d %B %Y"), (now.strftime("               %X")))
    print("-" * 40)
    print("  Pesanan         Jumlah         Harga")
    print("-" * 40)
    while ("Bakso" in pesanan):
        print("   Bakso            " +
              str(jumlahPesananBakso), "\t\t", (hargabakso))
        break
    while ("MieAyam" in pesanan):
        print(" Mie Ayam           " + str(jumlahPesananMieAyam),
              "  \t", (hargamieayam))
        break
    while ("TehManis" in pesanan):
        print(" Teh Manis          " + str(jumlahPesananTehManis),
              "\t\t", (hargatehmanis))
        break
    while ("Aqua" in pesanan):
        print("   Aqua             "+str(jumlahPesananAqua), "\t\t", (hargaaqua))
        break
    print("-" * 40,)
    print("Total       : Rp.", sblmdiskon)
    print("Discount    :", diskonpersen)
    print("Final Harga : Rp.", total)
    print("Tunai       : Rp.", uang)
    print("Kembalian   : Rp.", kembalian)
    print("-" * 40)
    print("Pembeli     :", nama)
    print("Nomer Meja  :", nomerMeja)
    print("-" * 40)
    print("TERIMAKASIH TELAH MAKAN DI BAKSO SELAMET\n")


awal()
daftarMenu()
kodeDiskon()
