import sys
import pyprimes

arg = int(sys.argv[1])

p = pyprimes.primes_below(arg)

total = 0
for i in p:
    total += i
print("Answer: ",total)
