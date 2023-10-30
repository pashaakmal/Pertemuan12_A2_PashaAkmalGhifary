from luas.persegi import Lpersegi
from luas.segitiga import Lsegitiga
from luas.lingkaran import Llingkaran
from luas.menu import mmenu

mmenu()

while True:
    choice = input("Pilih bentuk (1/2/3/4): ")
    if choice == "1":
        Lpersegi()
    elif choice == "2":
        Llingkaran()
    elif choice == "3":
        Lsegitiga()
    elif choice == "4":
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    