class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def __str__(self):
        return f"Proizvod: {self.naziv}, Cijena: {self.cijena}, Dostupna količina: {self.dostupna_kolicina}"
    

skladiste = [
    Proizvod("Laptop", 7500, 10),
    Proizvod("Mobitel", 3500, 25),
]

def dodaj_proizvod(proizvod):
    skladiste.append(proizvod)