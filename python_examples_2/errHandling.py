x = int(input("x degerini giriniz : "))
y = int(input("y degerini giriniz : "))

try:
    print(x/y)       
except ZeroDivisionError :
    print("ikinci deger sifir girilemez")
except ValueError  :
    print("bu degerler kullanılamaz")