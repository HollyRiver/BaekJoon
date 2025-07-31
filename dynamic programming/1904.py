N = int(input())

np = 2
npp = 1

if N == 1 :
    print(1)
elif N == 2 :
    print(2)
else :
    for _ in range(N-2) :
        n = np + npp
        npp = np
        np = n%15746
        
    print(n%15746)