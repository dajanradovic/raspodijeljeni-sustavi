def prvi_i_zadnji(lista):
    return (lista[0], lista.pop())

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(prvi_i_zadnji(lista)) # (1, 10)

def maks_i_min(lista):
    return (max(lista), min(lista))

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

print(maks_i_min(lista)) # (250, 5)

def presjek(skup_1, skup_2):
    return skup_1.intersection(skup_2)

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

print(presjek(skup_1, skup_2)) # {4, 5}