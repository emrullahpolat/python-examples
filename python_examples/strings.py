name = "emrullah"
surname = "polat"
age = 25

#köşeli parantezin içine format ile değişkeni yerleştirdik
print("my name is {} {}".format(name,surname)) 

#dize numarasına göre sırasıyla yazdırıyoruz
print("my name is {1} {0}".format(name,surname)) 

#int parametre eklenir
print("my name is {} {} .I'm {} years old.".format(name,surname,str(age))) 

#float bir değerin kaç basamağa kadar yazılacağı
result = 200/700
print("result is {r:1.4}".format(r=result)) 