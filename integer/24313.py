a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if (a1*n0 + a0 <= c*n0) and (a1*2**16 + a0 <= c*2**16) :
    print(1)
else :
    print(0)