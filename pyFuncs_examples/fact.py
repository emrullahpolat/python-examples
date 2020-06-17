def faktoriyel(num):
    if not isinstance(num, int):
        raise TypeError("Tam sayı değişkeni giriniz...")
    if not num >= 0:
        raise ValueError("Pozitif değerler girilebilir...")

    def hesaplama(num):
        if num <= 1:
            return 1
        
        return num * hesaplama(num - 1)

    return hesaplama(num)

print(faktoriyel(-5))
