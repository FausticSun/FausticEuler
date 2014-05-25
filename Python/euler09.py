import sys
import math

arg = int(sys.argv[1])

for i in range(1,arg):
    for j in range(i+1,arg):
        if i + j + math.sqrt(i**2+j**2) == arg:
            print("Answer: ",i*j*math.sqrt(i**2+j**2))
