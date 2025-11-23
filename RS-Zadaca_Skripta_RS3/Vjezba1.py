import asyncio

async def dohvacanje_s_neta():
    
    await asyncio.sleep(3)  
    
    podaci = [x for x in range(1, 11)]

    print("Podaci dohvaćeni")
    
    return podaci

async def main():
    await dohvacanje_s_neta()
    

asyncio.run(main())
