def faktorial(n):
    hasil = 1
    for i in range(1, n+1):
        hasil = hasil + i
    return hasil

n = int(input('Masukkan bilangan: '))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if j == 1:
            print(faktorial(i), end=" ")
        print(j, end=" ")
    print()