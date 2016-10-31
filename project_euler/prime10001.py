

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**(0.5))+1, 2):
            if n % i == 0:
                return False
        return True

def gen_primes(n):
    primes = [2]
    count = 3
    while len(primes) < n:
        if is_prime(count):
            primes.append(count)
        count += 2
    return primes

print(gen_primes(10001))
