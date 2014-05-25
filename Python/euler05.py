import sys
import pyprimes

arg = int(sys.argv[1])

ans = 1
powa = 1
p = pyprimes.primes_below(arg)
for i in p:
    powa = 1
    while powa > 0:
        if i**powa < arg:
            powa = powa + 1
        else:
            ans = ans*i**(powa-1)
            break
print('Answer: ', ans)
