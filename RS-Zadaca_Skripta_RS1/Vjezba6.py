# 1)  Suma brojeva od 1 do 100


# FOR petlja
suma = 0

for i in range(1, 101):
    suma += i

print(suma)

# WHILE petlja
suma = 0
counter = 1
while counter <= 100:
    suma += counter
    counter += 1

print(suma)


# 2 ) Ispisati unazad prvih 10 neparnih brojeva

# FOR petlja
neparniBrojevi = []

for i in range(1, 20, 2): 
    neparniBrojevi.append(i)

for i in range(len(neparniBrojevi) - 1, -1, -1):
    print(neparniBrojevi[i])


# WHILE petlja

neparniBrojevi = []
counter = 1

while True:
    if len(neparniBrojevi) == 10:
        break
   
    if counter % 2 != 0:
        neparniBrojevi.append(counter)
   
    counter += 2

counter = len(neparniBrojevi) - 1

while counter >= 0:
    print(neparniBrojevi[counter])
    counter -= 1


# 3) FIBONNACIJEVI BROJEVI DO 1000

# FOR PETLJA

fibonacci = [0, 1]
for i in range(1, 1000):
    next_fib = fibonacci[-1] + fibonacci[-2]
    if next_fib > 1000:
        break
    fibonacci.append(next_fib)

for i in fibonacci:
    print(i)

# WHILE PETLJA

fibonacci = [0, 1]
while True:
    next_fib = fibonacci[-1] + fibonacci[-2]
    if next_fib > 1000:
        break
    fibonacci.append(next_fib)

total = len(fibonacci) - 1
counter = 0

while counter <= total:
    print(fibonacci[counter])
    counter += 1
