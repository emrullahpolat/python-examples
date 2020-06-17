# x = 10
# if x > 5:
#     raise Exception("x degeri 5den buyuk olamaz")

def check_pass(pasw):
    import re
    if len(pasw) < 8:
        raise Exception("parola en az 8 karakter olmalıdır...")
    elif not re.search("[a-z]",pasw):
        raise Exception("kucuk harfli karakterler girilmelidir...")
    elif not re.search("[A-Z]",pasw):
        raise Exception("Buyuk Harf Girmelisiniz...")
    elif not re.search("[_@.$]",pasw):
        raise Exception("alpha numerik değer girilmelidir...")
    elif re.search("[\s]",pasw):
        raise Exception("Bosluk degeri girilemez...")
    else:
        print("gecerli parola")

password = "123456Za_"

try:
    check_pass(password)
except Exception as err:
    print(err)