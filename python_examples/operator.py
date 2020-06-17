a = b = [1,2,3]
c = [1,2,3]

print(a == b)
print(a==c)

#burada hafızadaki adres konumları karşılaştırıldı
print("a ve b -> ",a is b)
print("a ve c -> ",a is c)

#bir dizide kontrol
name = "emrullah"
print('l' in name)