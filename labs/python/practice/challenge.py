# calculating primes numbers in 0 to 250 store values results.txt

limit = 250
primeNumbers = []
isPrime = [True] * (limit + 1)


for prime in range(2, limit + 1):
    if isPrime[prime]:
        primeNumbers.append(prime)

        # filter loop
        for even in range(prime * prime, limit + 1, prime):
            isPrime[even] = False # 2*2,  3*3..... 0 , 1


print(primeNumbers)


with open ("results.txt", 'a') as file:
    file.write(str(primeNumbers))



    





