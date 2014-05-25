import sys

arg = int(sys.argv[1])

def checkDividable(num,digits):
    for i in range(10**digits,10**(digits+1)):
        if num%i == 0:
            print(i)
            return True
    return False

def palindromes(digits):
    for i in reversed(xrange(10**digits,10**(digits+1))):
        yield int(str(i)+str(i)[::-1])

d = arg-1
p = palindromes(d)
for i in p:
    if checkDividable(i,d):
        print("Answer: ", i)
