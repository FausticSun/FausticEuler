import sys
import pyprimes

arg = int(sys.argv[1])
p = pyprimes.primes_below(arg)

for i in p:
    #print('Testing: ', i)
    if arg%i == 0:
        print('Prime factor: ', i)
