N, K = map(int, input().split())

fac = [1]

for i in range(2, N//2 + 1) :
    if N % i == 0 :
        fac.append(i)

fac.append(N)

if len(fac) >= K :
    print(fac[K-1])
else :
    print(0)