# Objasnite korak po korak kako se ponaša event loop (kako se raspoređuju, izvršavaju i dovršavaju korutine te koja su njihova stanja u 
# različitim fazama izvođenja) na sljedećem primjeru:

import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    await asyncio.gather(*timers)

asyncio.run(main())


'''
1) u event loop-u pocinje se izvrsavati prva kortuina - main - u njoj vidimo listu sa 3 schedulene korutine kreirane s asyncio.crate_task() metodom 
2) dolazimo do linije asyncio.gather koja suspendira izvrsavanje main korutine na even loop-u i pokrece izvrsavanje prve korutine u listi s nazivom Timer 1
3) u Timer 1 se pokreće for petlja i nailazi na asyncio.sleep metodu koja suspendira korutinu Timer 1 u event loopu
4) event loop ide dalje te nailazi na korutinu Timer 2
4) korutina Timer 2 pokreće for petlju i nailazi na asyncio.sleep korutinu koja suspendira Timer 2 korutinu u event loopu
5) event loop ide dalje te nailazi na korutinu Timer 3
5) korutina Timer 3 pokreće for petlju i nailazi na asyncio.sleep korutinu koja suspendira korutinu Timer 3 u event loopu 
6) event loop ne pronalazi nove korutine pa se vraća u Timer 1 gdje se petlja nastavlja te u drugoj iteraciji ponovo nailazi na asyincio.sleep korutinu
 te se nakon toga slijed događaja ponavlja dok se ne izvrše sve 3 korutine  (nakon što najkraća korutina zavrsi slijed događaka će se ponavaljati između 
 preostale dvije korutijne te tako dok posljednja ne završi te se nakon toga event loop čisti tj ostaje prazan) i to je kraj
'''