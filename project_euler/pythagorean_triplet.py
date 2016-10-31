

def triplet():
    for a in range(1,500):
        for b in range(a,500):
            c_squared = a**2+b**2
            c = c_squared**(0.5)
            if c - int(c) == 0:
                c = int(c)
            else:
                continue
            if a+b+c == 1000:
                return [(a,b,c), (a**2+b**2), (a+b+c), (a<b<c)]

    

print(200*375*425)
print(triplet())




