import sys

a,b,c = (int(i) for i in input().split())
output = a * 2
if c >= 2:
    if b != 0:
        output += b*2 + 3
        c -= 2
    output +=(c//2)*3
    # if c > 2:
    #     output += (c - 2) * 3
print(output)