brojZaPogoditi = 45

broj_je_pogoden = False

brojPokusaja = 0

while not broj_je_pogoden:
    uneseniBroj = int(input("Unesite broj izmedju 1 i 100: "))
    brojPokusaja += 1

    if uneseniBroj < brojZaPogoditi:
        print("Uneseni broj je manji od trazenog broja.")
    elif uneseniBroj > brojZaPogoditi:
        print("Uneseni broj je veci od trazenog broja.")
    else: 
        print("Uneseni broj je jednak trženom broju.")
        broj_je_pogoden = True

print(f"Bravo, pogodio si u {brojPokusaja} pokusaja!")