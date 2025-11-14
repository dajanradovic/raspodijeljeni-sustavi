import datetime
from functools import reduce

# 1.

class Automobil:

    def __init__(self, marka, model, godina_proizvodnje, kilometraža):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraža = kilometraža

    def ispisi_informacije(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraža: {self.kilometraža} km")

    def starost(self):
        trenutna_godina = datetime.datetime.now().year
        
        print(trenutna_godina - self.godina_proizvodnje)
    
a = Automobil("Toyota", "Corolla", 2011, 75000)
a.ispisi_informacije()
a.starost()


# 2.
class Kalkulator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Dijeljenje s nulom nije dozvoljeno."
    
    def potenciranje(self):
        return self.a ** self.b   
    
    def korijen(self):
        if self.a >= 0:
            return self.a ** 0.5
        else:
            return "Nije moguće izračunati korijen negativnog broja."
        
k = Kalkulator(16, 4)

print(k.zbroj())
print(k.oduzimanje())
print(k.mnozenje())
print(k.dijeljenje())
print(k.potenciranje())
print(k.korijen())


# 3.
class Student:

    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def ispisi_informacije(self):
        print(f"Ime: {self.ime}")
        print(f"Prezime: {self.prezime}")
        print(f"Godine: {self.godine}")
        print(f"Ocjene: {self.ocjene}")

    def prosjek_ocjena(self):
        if len(self.ocjene) > 0:
            return sum(self.ocjene) / len(self.ocjene)
        else:
            return 0
    

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = []

for s in studenti:
    student = Student(s["ime"], s["prezime"], s["godine"], s["ocjene"])
    studenti_objekti.append(student)

najbolji_student = reduce(lambda s1, s2: s1 if s1.prosjek_ocjena() > s2.prosjek_ocjena() else s2, studenti_objekti)
   
print(najbolji_student.ime, najbolji_student.prezime, najbolji_student.prosjek_ocjena())


# 4.

class Krug:

    def __init__(self, r):
        self.r= r

    def opseg(self):
        print(2 * self.r * 3.14)
        
    def povrsina(self):
        print(3.14 * (self.r ** 2))
    

k = Krug(5)

k.opseg()
k.povrsina()


# 5.

class Radnik:
        
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}.")

class Menadzer(Radnik):
    
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}.")

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje

radnik = Radnik("David", "SysAdmin", 5000)
menadzer = Menadzer("Matija", "Menadzer", 8000, "IT")
radnik.work()   
menadzer.work() 
menadzer.give_raise(radnik, 1000)
print(radnik.placa)