import sys

arg = int(sys.argv[1])

def rangeSum(x): 
    return x/2*(x+1) if x%2==0 else x/2*(x+1)+x/2+1

arg = arg - 1

print("Answer: ", 3*rangeSum(arg/3)+5*rangeSum(arg/5)-15*rangeSum(arg/15))


