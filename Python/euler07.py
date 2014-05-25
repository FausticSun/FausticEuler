import sys
import pyprimes

arg = int(sys.argv[1])

p = pyprimes.nprimes(arg)
ans = 0
for i in p:
    ans = i
print('Answer: ', ans)
