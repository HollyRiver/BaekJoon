from sys import stdin

N, M = map(int, stdin.readline().split())

A = [0]*N

for i in range(N) :
    A[i] = list(map(int, stdin.readline().split()))
    
for i in range(N) :
    input_list = list(map(int, stdin.readline().split()))
    
    for j in range(M) :
        A[i][j] += input_list[j]
    

print("\n".join([" ".join([str(t) for t in rw]) for rw in A]))