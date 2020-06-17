class Matematik:
    def __init__(self,sayi1,sayi2):
        self.s1 = sayi1
        self.s2 = sayi2
    def topla(self):
        return (self.s1 + self.s2)
    def cikar(self):
        return (self.s1 - self.s2)
    def carp(self):
        return (self.s1 * self.s2)
    def bol(self):
        return (self.s1 / self.s2)

matematik = Matematik(10,2)
sonuc = matematik.topla()
print(sonuc)