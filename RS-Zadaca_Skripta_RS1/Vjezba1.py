prviBroj = float(input('Unesi prvi broj: '))
drugiBroj = float(input ('Unesi drugi broj: '))
operator = input('Unesi operator: ')
moguciOperatori = ('+', '-', '/', '*')

if operator not in moguciOperatori:
    print('Nepodržani operator!')
elif drugiBroj == 0.0 and operator == '/':
    print('Dijeljenje s nulom nije dozvoljeno!')
else:

    rez = 0

    if operator == '+':
        rez = prviBroj + drugiBroj
    elif operator == '-':
        rez = prviBroj - drugiBroj
    elif operator == '*':
        rez = prviBroj * drugiBroj
    else:
        rez = prviBroj / drugiBroj

    print(f"Rezultat operacije {prviBroj} {operator} {drugiBroj} je {rez}")
