def filtriraj_parne(list):
    filteredList = []
   
    for num in list:
        if num % 2 == 0:
            filteredList.append(num)

    return filteredList

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filtriraj_parne(lista))