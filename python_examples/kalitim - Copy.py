class Personalty:
    def __init__(self,frstName,surname,birthPlace):
        self.frstname = frstName
        self.surname = surname
        self.birthPlace = birthPlace
        
        #print("bir birey olusturuldu.")

class Physical:
    def __init__(self,height,age,eyeColor,gender):
        self.height = height
        self.gender = gender
        self.age = age
        self.eyeColor = eyeColor

class Jobs:
    def __init__(self, company, degree, job):
        self.company = company
        self.degree = degree
        self.job = job

class Person(Personalty,Jobs,Physical):
    def __init__(self):
        Personalty.__init__(self)
        print("Ogretmen olusturuldu.")

person1 = Person()
