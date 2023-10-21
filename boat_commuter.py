import sys
from typing import List

lone = []
n,m,k = (int(i) for i in input().split())
map = [0] * (m + 1)
vals =[0] * (m + 1)
for i in range(k):
    a,b = (int(i) for i in input().split())
    if map[b] == 0:
        map[b] = a
    elif map[b] == a:
        map[b] = 0
        vals[b] += 100
    else:
        vals[b] += abs(map[b] - a)
        map[b] = 0

print(vals)
output = ""
# sep = ' '
# test = sep.join(str(vals))
for i in range(1, m + 1):
    if map[i] > 0:
        vals[i] += 100
    output = output + str(vals[i]) + " "
    
# l = list(range(5))

    
print(test)

# vals: List[str] = ["g", "g", "y" ]

        

