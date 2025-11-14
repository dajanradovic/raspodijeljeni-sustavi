from shop import proizvodi
from shop import narudzbe

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for p in proizvodi_za_dodavanje:
    proizvodi.dodaj_proizvod(proizvodi.Proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"]))


for proizvod in proizvodi.skladiste:
    print(proizvod)

narudzbe_za_izradu = []
narudzbe_za_izradu.append(narudzbe.napravi_narudzbu(proizvodi_za_dodavanje))

for n in narudzbe_za_izradu:
    if n:
        n.ispis()