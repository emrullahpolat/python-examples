def bolme1(num1):

    def inner(num2):
        if num2 == 0:
            raise ValueError("payda degeri sıfır olamaz") 
        return num1/num2
    
    return inner

payda = bolme1(10)
print(payda(2))

def islem(islem_adi):
    def topla(number1, number2):
        return number1+number2
    
    def cikar(number1, number2):
        return number1-number2
    
    def bolme(number1,number2):
        return number1/number2
    
    def carp(number1,number2):
        return number2*number1

    if islem_adi == "topla":
        return topla
    if islem_adi == "cikar":
        return cikar
    if islem_adi == "bol":
        return bolme
    if islem_adi == "carp":
        return carp

print("ikinci fonksiyon\n")
islem1 = islem("topla")
print(islem1(10,5))