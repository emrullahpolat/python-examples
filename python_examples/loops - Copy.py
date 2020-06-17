sozluk = { 'adı' : 'emrullah', '^yasi': 19, 'milleti': 'Turkiye'}
for item1,item2 in sozluk.items():
    print(item2)

#while dongusu için
# i=1
# while i<=20:
#     i = i+1
#     if i%2==1:
#         print(f"sayi tekdir {i}")
#     else:
#         print(f"sayi cifttir {i}")
# print("bitti -> ",i)

#sayi dizisini sıralama
# sayi_dizisi = []
# x=1
# while x<=5:
#     sayi = int(input(". sayiyi giriniz"))
#     sayi_dizisi.append(sayi)
#     x +=1
# sayi_dizisi.sort()
# print(sayi_dizisi)

#dictionary halinde kullanıcıdan ürün verisi alma
# girdi = int(input("kac adet veri giriceksiniz : "))
# product = []
# x = 1
# y = 1
# while x <= girdi:
#      name= input("urun adını giriniz : ")
#      price= int(input("urun fiyatini giriniz : "))
#      product.append({
#          'name': name,
#          'price': price
#      })
#      x += 1

# while y < len(product):
#      print(product)
#      y += 1

#for özelliği ------
numbers = [x for x in range(10)]
print(numbers)

numbers_mod = [x**2 for x in range(12) if x%3==0]
print("3'le mod -> ",numbers_mod)

name = "Emrullah"
myName = [harfler for harfler in name]
print(myName)

result = [x if x%2==0 else "tek sayi" for x in range(1,10)]
print(result)

result = [(x,y) for x in range(3) for y in range(3)]
print(result)

