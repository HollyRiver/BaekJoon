import math
from sys import stdin

n, p, Q = map(float, stdin.readline().split())
n = int(n)
Q = int(Q)

lst = [[0]*2]*Q

for i in range(Q) :
    lst[i] = list(map(int, stdin.readline().split()))


if n*p < 30 :
    P_x = [math.log(math.comb(n, i)) + i*math.log(p) + (n-i)*math.log(1-p) for i in range(n+1)]
    print("\n".join([str(max([sum([P_x[lst[k][0]:lst[k][1]+1][i] >= P_x[lst[k][1]-j] for i in range(lst[k][1]-lst[k][0]+1)])*P_x[lst[k][1]-j] for j in range(lst[k][1]-lst[k][0]+1)])) for k in range(Q)]))
else :
    