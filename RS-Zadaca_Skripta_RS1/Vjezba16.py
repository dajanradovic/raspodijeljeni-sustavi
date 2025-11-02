import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

def dijkstra(graph, start):
    
    pocetneUdaljenosti = {}

    for cvor in graph:
        if cvor == start:
            pocetneUdaljenosti[cvor] = 0
        else:
            pocetneUdaljenosti[cvor] = float('inf') # za beskonacno

    prioritet = [(0, start)]  

    while prioritet:
        trenutniPrioritet = heapq.heappop(prioritet)

        if trenutniPrioritet[0] > pocetneUdaljenosti[trenutniPrioritet[1]]:
            continue

        for susjedniCvor, velicinaUdaljenosti in graph[trenutniPrioritet[1]]:

            udaljenost = trenutniPrioritet[0] + velicinaUdaljenosti

            if pocetneUdaljenosti[susjedniCvor] > udaljenost:
                pocetneUdaljenosti[susjedniCvor] = udaljenost
                heapq.heappush(prioritet, (udaljenost, susjedniCvor))

    return pocetneUdaljenosti

print(dijkstra(graph, 'A'))

