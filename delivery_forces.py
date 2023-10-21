import sys
n = sys.stdin.readline()
staff = [int(i) for i in sys.stdin.readline().split()]
staff.sort()
staff.reverse()
total = 0
count = 0
i = 1
while count < int(n) // 3:
    total += staff[i]
    i += 2
    count += 1
print(total)
