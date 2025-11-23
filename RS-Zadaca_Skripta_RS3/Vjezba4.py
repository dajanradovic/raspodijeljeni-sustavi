import asyncio
import random

async def provjeri_parnost(broj):

    await asyncio.sleep(2) 

    if broj % 2 == 0:
        return f'Broj {broj} je paran.'
    
    return f'Broj {broj} je neparan.'

async def main():

    random_brojevi = [random.randint(1, 100) for _ in range(10)]

    tasks = [asyncio.create_task(provjeri_parnost(i)) for i in random_brojevi]

    rezultati = await asyncio.gather(*tasks)

    print(rezultati)

asyncio.run(main())
