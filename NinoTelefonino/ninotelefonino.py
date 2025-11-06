phoneDictionaryData = [
    {"Pozivni broj": "01", "Mjesto / Operater": "Grad Zagreb i Zagrebačka županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "020", "Mjesto / Operater": "Dubrovacko-neretvanska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "021", "Mjesto / Operater": "Splitsko-dalmatinska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "022", "Mjesto / Operater": "Šibensko-kninska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "023", "Mjesto / Operater": "Zadarska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "031", "Mjesto / Operater": "Osječko-baranjska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "032", "Mjesto / Operater": "Vukovarsko-srijemska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "033", "Mjesto / Operater": "Virovitičko-podravska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "034", "Mjesto / Operater": "Požeško-slavonska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "035", "Mjesto / Operater": "Brodsko-posavska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "040", "Mjesto / Operater": "Međimurska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "042", "Mjesto / Operater": "Varaždinska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "043", "Mjesto / Operater": "Bjelovarsko-bilogorska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "044", "Mjesto / Operater": "Sisačko-moslavačka županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "047", "Mjesto / Operater": "Karlovačka županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "048", "Mjesto / Operater": "Koprivničko-križevačka županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "049", "Mjesto / Operater": "Krapinsko-zagorska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "051", "Mjesto / Operater": "Primorsko-goranska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "052", "Mjesto / Operater": "Istarska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "053", "Mjesto / Operater": "Ličko-senjska županija", "Vrsta": "Fiksna mreža"},
    {"Pozivni broj": "091", "Mjesto / Operater": "A1 Hrvatska", "Vrsta": "Mobilna mreža"},
    {"Pozivni broj": "092", "Mjesto / Operater": "Tomato", "Vrsta": "Mobilna mreža"},
    {"Pozivni broj": "095", "Mjesto / Operater": "Telemach", "Vrsta": "Mobilna mreža"},
    {"Pozivni broj": "097", "Mjesto / Operater": "bonbon", "Vrsta": "Mobilna mreža"},
    {"Pozivni broj": ('098', '099'), "Mjesto / Operater": "Hrvatski Telekom", "Vrsta": "Mobilna mreža"},
    {"Pozivni broj": "0800", "Mjesto / Operater": "Besplatni pozivi", "Vrsta": "Posebne usluge"},
    {"Pozivni broj": "060", "Mjesto / Operater": "Komercijalni pozivi", "Vrsta": "Posebne usluge"},
    {"Pozivni broj": "061", "Mjesto / Operater": "Glasovanje telefonom", "Vrsta": "Posebne usluge"},
    {"Pozivni broj": "064", "Mjesto / Operater": "Usluge s neprimjerenim sadržajem", "Vrsta": "Posebne usluge"},
    {"Pozivni broj": "065", "Mjesto / Operater": "Nagradne igre", "Vrsta": "Posebne usluge"},
    {"Pozivni broj": "069", "Mjesto / Operater": "Usluge namijenjene djeci", "Vrsta": "Posebne usluge"},
    {"Pozivni broj": "072", "Mjesto / Operater": "Jedinstveni pristupni broj za cijelu državu za posebne usluge", "Vrsta": "Posebne usluge"},
]


def validiraj_broj_telefona(broj: str):

    result = {
        "pozivni_broj": '',
        "broj_ostatak": '',
        "vrsta": '',
        "mjesto" : None,
        "operater": None,
        "validan": False
    }
    
    broj = sanitiziraj_broj_telefona(broj)
    
    pozivniDrzave = izvuci_pozivni_broj_drzave(broj)

    brojBezPozivnogDrzave = izvuci_broj_bez_pozivnog_drzave(broj, pozivniDrzave)

    ditionaryInfo = pronadi_info_po_pozivnom_broju(brojBezPozivnogDrzave, bool(pozivniDrzave))
    
    pozivniBroj = ditionaryInfo.get("Pozivni broj", '')

    result["pozivni_broj"] = pozivniDrzave + pozivniBroj
    
    vrsta = ditionaryInfo.get("Vrsta", '')

    result["vrsta"] = vrsta

    brojOstatak = brojBezPozivnogDrzave[len(pozivniBroj):]

    result["broj_ostatak"] = brojOstatak

    if(vrsta not in ("Mobilna mreža", "Posebne usluge")):
        result["mjesto"] = ditionaryInfo.get("Mjesto / Operater", '')

    if(vrsta not in ("Posebne usluge", "Fiksna mreža")):
        result["operater"] = ditionaryInfo.get("Mjesto / Operater", '')

    brojOstatakValidan = validiraj_broj_ostatak(brojOstatak, vrsta)

    if brojOstatakValidan and pozivniBroj and vrsta:
        result["validan"] = True

    return result

def sanitiziraj_broj_telefona(broj: str):

    allowedChars = set("0123456789+")

    broj = ''.join(c for c in broj if c in allowedChars)

    return broj

def izvuci_pozivni_broj_drzave(broj: str):

    drzavniPredznak = ("+385", "385", "00385")
    pozivniDrzave = ''

    for predznak in drzavniPredznak:
        if broj.startswith(predznak):
            pozivniDrzave = predznak
          
            break

    return pozivniDrzave

def izvuci_broj_bez_pozivnog_drzave(broj: str, pozivniDrzave: str):

    if pozivniDrzave:
        ostaliBroj = broj.split(pozivniDrzave, 1)[1]
    else:
        ostaliBroj = broj

    return ostaliBroj

def pronadi_info_po_pozivnom_broju(broj: str, imaPozivniBrojDrzave: bool):
    
    for entry in phoneDictionaryData:
       
        pozivni = entry["Pozivni broj"]
       
        if isinstance(pozivni, tuple):
            for p in pozivni:
                res = pronadi_info(broj, p, imaPozivniBrojDrzave, entry)
                if res:
                   return res
                    
        else:
            res = pronadi_info(broj, pozivni, imaPozivniBrojDrzave, entry)
            if res:
                return res

    return {}

def pronadi_info(broj: str, pozivniBroj: str, imaPozivniBrojDrzave: bool, entry: dict):
    
    pozivniBrojDictionaryEntry = {}

    if not imaPozivniBrojDrzave:
        
        if broj.startswith(pozivniBroj):
            pozivniBrojDictionaryEntry = entry
            pozivniBrojDictionaryEntry["Pozivni broj"] = pozivniBroj
            
    else:
        minusLeadingZero = pozivniBroj[1:]
        if broj.startswith(minusLeadingZero):
            pozivniBrojDictionaryEntry = entry
            pozivniBrojDictionaryEntry["Pozivni broj"] = minusLeadingZero

    return pozivniBrojDictionaryEntry


def validiraj_broj_ostatak(brojOstatak: str, vrsta: str):

    duzina = len(brojOstatak)

    if vrsta in ("Fiksna mreža", "Mobilna mreža"):
        if duzina in (6, 7):
            return True
  
    elif vrsta == "Posebne usluge":
        if duzina == 6:
            return True

    return False


ulazniBroj = input("Unesite broj telefona za validaciju: ")

print(validiraj_broj_telefona(ulazniBroj))