import asyncio

async def autentifikacija(korisnik):

    baza_korisnika = [
        {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
        {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
        {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
        {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
    ]

    await asyncio.sleep(3)

    result = [x for x in baza_korisnika if korisnik['korisnicko_ime'] == x['korisnicko_ime'] and x['email'] == korisnik['email']]

    if not result:
        print(f"Korisnik {korisnik} nije pronađen.")

        return
    
    await autorizacija(result[0], korisnik['lozinka'])
    

async def autorizacija(pronadeni_korisnik, lozinka):

    baza_lozinka = [
        {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
        {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
        {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
        {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
    ]

    await asyncio.sleep(2)

    podudara_se_lozinka = any(map(lambda korisnik: True if korisnik['lozinka'] == lozinka and korisnik['korisnicko_ime'] == pronadeni_korisnik['korisnicko_ime'] else False, baza_lozinka))

    if not podudara_se_lozinka:
        print(f"Korisnik {pronadeni_korisnik}: Autorizacija neuspješna.")

    else:
        print(f"Korisnik {pronadeni_korisnik}: Autorizacija uspješna.")

async def main():

    await autentifikacija({'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com', 'lozinka': 'super_teska_lozinka'})

   
asyncio.run(main())
