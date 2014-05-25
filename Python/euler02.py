import sys

arg = int(sys.argv[1])

def fib(n):
    a,b = 0, 1
    while a<n:
        yield a
        a,b = b,a+b

total = 0
fibgen = fib(arg)
for i in fibgen:
    if i%2 == 0:
        total += i
print("Answer",total)
