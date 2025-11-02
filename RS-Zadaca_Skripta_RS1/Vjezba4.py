suma = 0

while True:
    broj = int(input("Unesite cijeli broj: "))
    if broj == 0:
        break
    else:
        suma = suma + broj  

print(f"Suma unesenih brojeva je: {suma}")
