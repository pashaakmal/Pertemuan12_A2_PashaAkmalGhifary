from luas.menu import mmenu
def Lsegitiga():
    print("Menghitung Luas Segitiga")
    a = float(input("Masukkan Alas : "))
    t = float(input("Masukkan Tinggi : "))
    luas = (a * t) / 2
    print("Luas Segitiga adalah ", luas)
    print()
    print("Coba lagi [Y/N]? ")
    back = input().upper()
    if back == "Y":
        mmenu()
    else:
        exit()