import sys

arg = int(sys.argv[1])

t1 = 0
t2 = 0
for i in range(1,arg):
    t1 += i**2
    t2 += i
print t2**2-t1
