from functools import reduce


def is_prime(n):
    if n%2 == 0 and n > 0:
        return False
    return all(n%i for i in range(3, int(n**(0.5))+1, 2))
        


def all_factors(n):
    flatten = lambda x,y: x+y
    tuple_facts = [(i, n//i) for i in range(2,int(n**(0.5))+1) if n%i==0]
    return set(reduce(flatten, tuple_facts))

def largest_prime_factor(n):
    prime_factors = [i for i in all_factors(n) if is_prime(i)]
    return max(prime_factors)
    

print(largest_prime_factor(600851475143))


