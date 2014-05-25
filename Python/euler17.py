import sys

arg = int(sys.argv[1])

def digit2count(i):
    return {
        1: 3,
        2: 3,
        3: 5,
        4: 4,
        5: 4,
        6: 3,
        7: 5,
        8: 5,
        9: 4,
        10: 3,
        11: 6,
        12: 6,
        13: 8,
        14: 8,
        15: 7,
        16: 7,
        17: 9,
        18: 8,
        19: 8,
        20: 6,
        30: 6,
        40: 6,
        50: 5,
        60: 5,
        70: 7,
        80: 6,
        90: 6
    }.get(i, 0)

def num2count(i):
    count = 0
    one = i%10
    ten = i//10%10
    hundred = i//100
    print(hundred,ten,one)
    if ten == 1:
        count += digit2count(ten*10+one)
    else:
        count += digit2count(one)
        count += digit2count(ten*10)
        print(digit2count(ten*10))
    if hundred != 0:
        count += digit2count(hundred) + 7 + 3
    return count

ans = 0
for i in range(arg):
    ans += num2count(i)
print(ans)
