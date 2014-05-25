import sys
import pyprimes

arg = int(sys.argv[1])

def triangleGen():
    n = 2
    while True:
        tri = 0
        for i in range(n):
            tri = tri + i
        yield tri
        n = n + 1

def numFactors(n):
    ct = 0
    l = []
    temp = n
    p = pyprimes.primes()
    for i in p:
        l.append(0)
        while temp%i==0:
            l[ct] += 1
            temp = temp/i
        ct += 1
        if temp==1:
            break
    num = 1
    for i in l:
        num *= i+1

    return num


g = triangleGen()
for i in g:
    factors = numFactors(i)
    print("Testing:", i, "Factors", factors)
    if factors > arg:
        print(i)
        break
