import sys, math
h1,d1,t1 = (int(i) for i in input().split())
h2,d2,t2 = (int(i) for i in input().split())

s1 = (math.ceil(h2 / d1) - 1) * t1
s2 = (math.ceil(h1 / d2) - 1) * t2
if s1 > s2:
    print("player two")
elif s1 < s2:
    print("player one")
else:
    print("draw")


