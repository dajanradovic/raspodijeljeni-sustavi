
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

def count_vowels_and_consonants(text):
    dictio = {
        'vowels': 0,
        'consonants': 0
    }
    
    for char in text:
        if char in vowels:
            dictio['vowels'] += 1
        elif char in consonants:
            dictio['consonants'] += 1

    return dictio

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(count_vowels_and_consonants(tekst))

