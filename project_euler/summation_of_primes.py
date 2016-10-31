

def eratosthenes(n):
    nums = [1]*n
    start = 2
    while start<len(nums):
        if nums[start] == 1:
            for i in list(range(start*2,len(nums),start)):
                nums[i] = 0
        start += 1
    primes = [e[0] for e in enumerate(nums) if e[1]][2:]
    return sum(primes)


print(eratosthenes(2000000))
