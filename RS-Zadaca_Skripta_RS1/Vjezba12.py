def obrni_rjecnik(rjecnik):
    final = {}
    for key,value in rjecnik.items():
        final[value] = key
    
    return final


rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

print(obrni_rjecnik(rjecnik))

# {'Ivan': 'ime', 'Ivić': 'prezime', 25: 'dob'}