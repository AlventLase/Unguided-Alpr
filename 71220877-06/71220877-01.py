def bilangan_prima(n): 
    if n == 2:
        return True
    elif n<= 0:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

n = int(input('Masukkan nilai n: '))
if n > 2:
    for i in range(n - 1, 1, -1):
        if bilangan_prima(i):
            print('bilang prima terdekat adalah: ', i)
            break
else:
    print('tidak ada')