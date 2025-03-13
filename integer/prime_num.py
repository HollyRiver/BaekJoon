## M이상 N이하의 소수를 모두 출력하는 프로그램
## 에라토스테네스의 체를 이용하여 풀이해야 함

M, N = map(int, input().split())

wdth = int((N**0.5)//1)
rnge = {i for i in range(2, wdth+1)}

for n in list(rnge) :
    for w in range(2, wdth+1) :
        if (w != n) & (n%w == 0) :
            rnge.remove(n)
            break

boundary_prime = sorted(list(rnge))
rnge = {i for i in range(M, N+1)}

rnge.discard(1)

for n in list(rnge) :
    for w in boundary_prime :
        if (w != n) & (n%w == 0) :
            rnge.remove(n)
            break

sorted_prime = sorted(list(rnge))

for n in sorted_prime :
    print(n)