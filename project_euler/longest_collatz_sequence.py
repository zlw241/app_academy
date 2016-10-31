

collatz_cache = {}

def collatz_recursive(n):
    if n == 1:
        return 1
    if n not in collatz_cache: 
        if n % 2 == 0:
            collatz_cache[n] = 1 + collatz_recursive(n//2)
        else:
            collatz_cache[n] = 1 + collatz_recursive(3*n+1)
    return collatz_cache[n]

def longest_collatz(upper_limit):
    all_collatz = [collatz_recursive(i) for i in range(1,upper_limit)]
    max_collatz = max(all_collatz)
    return all_collatz.index(max_collatz) + 1

print(longest_collatz(1000000))



