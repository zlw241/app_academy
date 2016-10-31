from functools import reduce


def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False

def all_factors(n):
    flatten = lambda x,y: x+y
    tuple_facts = [(i, n//i) for i in range(2,int(n**(0.5))+1) if n%i==0]
    try:
        return set(reduce(flatten, tuple_facts))
    except:
        return None

def is_palindromic_product(n,y):
    if is_palindrome(n*y):
        return True
    return False

def largest_palindromic_product(upper):
    palindrome = None
    start = upper**2
    while not palindrome and start > upper:
        if is_palindrome(start):
            if three_digits(start):
                x,y = three_digits(start)[0], three_digits(start)[1]
                if is_palindromic_product(x,y):
                    return start
        start -= 1
    return None

def three_digits(n):
    try:
        factors = [i for i in all_factors(n) if len(str(i)) == 3]
    except TypeError:
        return False
    if len(factors) > 1:
        sorted_facts = list(reversed(sorted(factors)))[:2]
        if sorted_facts[0] * sorted_facts[1] != n:
            return False
        return sorted_facts
    return False


print(largest_palindromic_product(999))







