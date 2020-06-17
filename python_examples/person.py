class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def name(self):
        return self.name

    def surname(self):
        return self.surname

musteri = Person("emrullah","polat")
musteri = Person("harun", "kayabasi")

print(musteri.name)

class Istatistik(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def varyans(self):
        return self.name + self.surname
    

