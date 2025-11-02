def brojanje_rijeci(tekst):
    dicto = {}
    for w in tekst.split(" "):
       if w not in dicto:
           dicto[w] = 1
       else:
           dicto[w] = dicto[w] + 1
    return dicto


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(brojanje_rijeci(tekst))