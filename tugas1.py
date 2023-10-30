import math

# Input koefisien dari keyboard
a = float(input('Masukkan a: '))
b = float(input('Masukkan b: '))
c = float(input('Masukkan c: '))

# hitung diskriminan d
d = (b**2) - (4*a*c)

# cek diskriminan
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print('Solusinya adalah {0} dan {1}'.format(x1, x2))
else:
    print("d harus lebih besar dari 0")
