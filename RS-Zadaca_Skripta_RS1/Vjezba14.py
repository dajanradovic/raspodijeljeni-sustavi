def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(isPrime(11)) 

def primes_in_range(start, end):
    primes = []
    for i in range(start, end):
       if isPrime(i):
            primes.append(i)
    return primes

print(primes_in_range(1, 10)) # [2, 3, 5, 7]
