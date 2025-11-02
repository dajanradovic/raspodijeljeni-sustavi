def ukloni_duplikate(listaa):
    uniqueSet = set()

    for num in listaa:
        uniqueSet.add(num)

    return list(uniqueSet)    

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(ukloni_duplikate(lista))