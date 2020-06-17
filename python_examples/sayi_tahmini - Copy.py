import random
rnd_sayi = random.randint(1,100)

yanlis_hakki = int(input("kac denemede bilmek istersiniz : "))

for x in yanlis_hakki:
    tahmin = int(input("tahmin degerini giriniz : "))
    if tahmin < rnd_sayi:
        print("sayinin altinda kaldiniz!!!")
    elif tahmin > rnd_sayi:
        print("sayiyi buyuk tahmin ettiniz :")
    elif tahmin == rnd_sayi:
        print(x,". adimda dogru bildiniz ")
    