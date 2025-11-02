def grupiraj_po_paritetu(lista):
    parni = []
    neparni = []

    for num in lista:
        if num % 2 == 0:
            parni.append(num)
        else:
            neparni.append(num)

    dictio = {
        'parni' : parni,
        'neparni' : neparni
    }

    return dictio

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(grupiraj_po_paritetu(lista))

# {'parni': [2, 4, 6, 8, 10], 'neparni': [1, 3, 5, 7, 9]}