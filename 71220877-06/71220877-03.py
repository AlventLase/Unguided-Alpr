tinggi = int(input('Masukkan tinggi: '))
lebar = int(input('Masukkan lebar: '))

luas = lebar * tinggi
angka = 0
while angka != luas:
    for i in range(lebar):
        angka += 1
        print(angka, end=' ')
    print()