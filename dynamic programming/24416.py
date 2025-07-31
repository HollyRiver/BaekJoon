from sys import stdin

n = int(stdin.readline().rstrip()) ## n >= 5

NREF = [1, 1]

for i in range(2, n) :
    NREF.append(NREF[i-1] + NREF[i-2])

print(f"{NREF[-1]} {n-2}")