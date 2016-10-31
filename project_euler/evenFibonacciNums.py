

def nthFib(n):
    first,second = 1, 2
    fibs = [first,second]
    count = 0
    while second < n:
        first,second = second, first+second
        fibs.append(second)
        count += 1 


    even_fibs = [i for i in fibs if i%2 == 0]
    return sum(even_fibs)



print(nthFib(4000000))
