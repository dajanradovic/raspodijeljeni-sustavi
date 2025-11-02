def provjera_lozinke(arg1):
    
    unallowedChars = ('password', 'lozinka')
    hasCapitalLetter = False
    hasDigit = False

    if  len(arg1) < 8 or len(arg1) > 15:
        print('Lozinka mora sadržavati između 8 i 15 znakova')
        return

    for unallowed in unallowedChars:
        if unallowed in arg1:
            print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
            return

    for letter in arg1:
        if letter.isdigit():
            hasDigit = True
            continue
        if letter.isupper():
            hasCapitalLetter = True
      
        if hasCapitalLetter and hasDigit:
            break
    
    if not hasCapitalLetter or not hasDigit:
       print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
       return

    print("Lozinka je jaka!")


lozinka = input('Unesite lozinku: ')

provjera_lozinke(lozinka)
