

def inefficient(n):
    divisors = range(n//2,n+1)
    success = False
    count = n
    while not success:
        if all((count%divisor==0 for divisor in divisors)):
            num = count
            success = True
        else:
            count += n
    return count

def efficient(target):
    n = 1
    for i in range(1,target+1):
        for j in range(1,target+1):
            if (n * j) % i == 0:
                n *= j
                break
    return n

print(inefficient(10))
print(efficient(20))









