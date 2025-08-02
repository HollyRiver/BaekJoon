from sys import stdin

N, Q = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

p = 0
r = N-1
result = 0

if A == B :
    result = 1

while p != r :
    j = p-1
    
    for i in range(p, r) :
        if A[i] <= A[r] :
            j += 1
            if i != j :
                Ai = A[i]
                A[i] = A[j]
                A[j] = Ai
            
                if A == B :
                    result = 1
    
    j += 1 ## 첫 번째로 큰 값의 인덱스(파티션)
    
    if j != r :
        Aj = A[j]
        A[j] = A[r]
        A[r] = Aj
        
        if A == B :
            result = 1

    if result != 0 :
        break
    
    if j > Q-1 :
        # p = p ## p는 그대로
        r = j-1
    
    elif j < Q-1 :
        # r = r ## r은 그대로
        p = j+1
    
    else :
        break ## A[j]가 Q번째 값

if p == r :
    j = r

print(result)