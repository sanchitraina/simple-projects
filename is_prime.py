import math, time
start = time.time()
primes = []
def add_prime():
    for i in range(0, (10 ** 4) + 1):
        if is_prime(i):
            primes.append(i)

def is_prime(num):
    prime = True
    if num == 0 or num == 1:
        prime = True
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                prime = False
                break
    return prime

add_prime()
print(time.time() - start, 'seconds')
