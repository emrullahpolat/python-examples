urunler = ["laptop", "mause", "telgraf"]

print(urunler)
print(type(urunler))

urunler.append("kablo")
print(urunler)

sinif1 = ["e","m","c"]
sinif2 = ["a","b","p","r"]
temp =sinif1

sinif1 = sinif2
sinif2[2] = "emrullah"
print(sinif1)
print(temp)