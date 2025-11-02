for i in range(1, 2):
    print(i)    # petlja ce se izvrsiti samo jednom jer range ide do 2, ali ne ukljucuje 2 (ispisat ce samo broj 1)

for i in range(10, 1, -2):
    print(i)    # petlja ce ispisati brojeve od 10 do 2, unazad, sa korakom 2 (10, 8, 6, 4, 2)

for i in range(10, 1, -1):
    print(i)    # petlja ce ispisati brojeve od 10 do 2, unazad, sa korakom 1 (10, 9, 8, 7, 6, 5, 4, 3, 2)
