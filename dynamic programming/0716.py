      
from sys import stdin

T = int(stdin.readline().rstrip())

lst = [[0]*14 for _ in range(15)]
lst[0] = [i for i in range(1, 15)]

for i in range(1, 15) :
    lst[i][0] = 1
    for j in range(1, 14) :
        lst[i][j] = lst[i][j-1] + lst[i-1][j]

for _ in range(T) :
    k = int(stdin.readline().rstrip())
    n = int(stdin.readline().rstrip())
    
    print(lst[k][n-1])
    
##-----------------------------------

A, B, V = map(int, input().split())

dpd = A-B

if dpd*((V-B)//dpd)+A == V :
    print((V-B)//dpd + 1)
elif dpd*((V-B)//dpd)+A > V :
    print((V-B)//dpd)
else :
    print((V-B)//dpd + 2)
    
    
A, B, V = map(int, input().split())

dpd = A-B

if (V-A)%dpd == 0 :
    print((V-A)//dpd + 1)
else :
    print((V-A)//dpd + 2)
    
##-----------------------------------

N = int(input())

output = "SciComLove\n"*N

print(output[:-1])