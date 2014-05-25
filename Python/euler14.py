import sys

arg = int(sys.argv[1])

def collatzTerms(n):
    terms = 1
    current = n
    while current != 1:
        terms += 1
        current = current/2 if current%2==0 else 3*current+1
    return terms

maxChains = 0
cause = 0
for i in range(arg,1,-1):
    print(i)
    chains = collatzTerms(i)
    if chains > maxChains:
        maxChains = chains
        cause = i
print("Answer: ",cause)
