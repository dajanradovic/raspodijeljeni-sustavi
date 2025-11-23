import asyncio

async def secure_data(podaci):

    await asyncio.sleep(3) 

    return {key: (hash(podaci[key]) if key in ["broj_kartice", "cvv"] else podaci[key]) for key in podaci}


async def main():

    rjecnici_osjetljivih_podataka = [
        {"prezime": "Ivić", "broj_kartice": "12345", "cvv": "123"},
        {"prezime": "Marković", "broj_kartice": "67890", "cvv": "456"},
        {"prezime": "Anić", "broj_kartice": "11223", "cvv": "789"},
    ]

    tasks = [asyncio.create_task(secure_data(podatak)) for podatak in rjecnici_osjetljivih_podataka]

    rezultati = await asyncio.gather(*tasks)

    print(rezultati)

asyncio.run(main())
