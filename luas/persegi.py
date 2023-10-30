from luas.menu import mmenu
def Lpersegi():
    print("Menghitung Luas Persegi Panjang")
    p = float(input("Masukkan Panjang : "))
    l = float(input("Masukkan Lebar : "))
    luas = p * l
    print("Luas Persegi Panjang adalah ", luas)
    print()
    print("Coba lagi [Y/N]? ")
    back = input().upper()
    if back == "Y":
        mmenu()
    else:
        exit()