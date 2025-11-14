class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis(self):
        print("Naručeni proizvodi:")
        print(self.naruceni_proizvodi)
        list(map(lambda x: print(f"{x['naziv']} x {x['dostupna_kolicina']}"), self.naruceni_proizvodi))
        print(f"Ukupna cijena: {self.ukupna_cijena}")
      

def napravi_narudzbu(proizvodi):
    if not isinstance(proizvodi, list) and not proizvodi:
        return
    if not all(map(lambda x: isinstance(x, dict), proizvodi)):
        return 
    if not all(map(lambda x: "naziv" in x and "cijena" in x and "dostupna_kolicina" in x, proizvodi)):
        return
    
    proizvodiBezKolicine = [proizvod for proizvod in proizvodi if proizvod["dostupna_kolicina"] <= 0] 

    if proizvodiBezKolicine:
        list(map(lambda x: print(f"Proizvod {x['naziv']} nije dostupan!"), proizvodiBezKolicine))
        return
    
    naruceni_proizvodi = proizvodi
    ukupna_cijena = sum(map(lambda x: x["cijena"] * x["dostupna_kolicina"], proizvodi))
   
    return Narudzba(naruceni_proizvodi, ukupna_cijena)