sayi = int(input("hesaplanicak sayiyi giriniz : "))
deger = 1

for i in range(1,sayi+1):
    deger = deger * i

print(sayi, " faktoriyeli : ", deger)