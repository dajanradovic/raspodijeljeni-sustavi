import asyncio

async def dohvacanje_podataka_o_korisnicima():
    
    await asyncio.sleep(3)  
    
    podaciOKorisnicima = [
        {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
        {"ime": "Marko", "prezime": "Marković", "godine": 22},
        {"ime": "Ana", "prezime": "Anić ", "godine": 21},
        {"ime": "Petra", "prezime": "Petrić", "godine": 13},
        {"ime": "Iva", "prezime": "Ivić", "godine": 17},
        {"ime": "Mate", "prezime": "Matić", "godine": 18}
   
    ]

    return podaciOKorisnicima


async def dohvacanje_podataka_o_proizvodima():
    
    await asyncio.sleep(5)  
    
    podaciOProizvodima = [
       {"naziv": "Laptop", "cijena": 7500, "kolicina": 5},
       {"naziv": "Monitor", "cijena": 1500, "kolicina": 15},
       {"naziv": "Tipkovnica", "cijena": 300, "kolicina": 30},
       {"naziv": "Miš", "cijena": 150, "kolicina": 80}
   
    ]

    return podaciOProizvodima

async def main():
   podaci_o_korisnicima, podaci_o_proizvodima = await asyncio.gather(
       dohvacanje_podataka_o_korisnicima(),
       dohvacanje_podataka_o_proizvodima()
   )
   print(f'Podaci_o_korisnicima: {podaci_o_korisnicima}')
   print(f'Podaci_o_proizvodima: {podaci_o_proizvodima}')
   
asyncio.run(main())
