## Quick Select : Theta(n), O(n^2)

from sys import stdin, setrecursionlimit

setrecursionlimit(12000)

N, Q, K = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

count = 0
result = "-1"

def partition(A, p, r) :
    global K
    global count
    global result
    
    x = A[r] ## 마지막 원소
    i = p-1
    
    for j in range(p, r) :
        if A[j] <= x :
            i += 1
            ai = A[i]
            A[i] = A[j]
            A[j] = ai
            count += 1
            
            if count == K :
                result = f"{A[i]} {A[j]}"
    
    ## 범위 내에서 자신보다 더 작은 값만 있는 쪽으로 밀어냄
    if i + 1 != r :
        aii = A[i+1]
        A[i+1] = A[r]
        A[r] = aii
        count += 1
        
        if count == K :
            result = f"{A[i+1]} {A[r]}"
        
    return i + 1

def select(A, p, r, q) :
    ## 범위가 단위 원소인 경우
    if p == r :
        return A[p]
    
    t = partition(A, p, r) ## 행렬을 2분할
    k = t-p+1
    
    if q < k :
        return select(A, p, t-1, q)
    
    elif q == k :
        return A[t]
    else :
        return select(A, t+1, r, q-k)


total_k = select(A, 0, N-1, Q)
print(result)


## 재귀 없이 구현 -> 더 빠름
from sys import stdin

N, Q, K = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

p = 0
r = N-1
k = 0
result = None

while p != r :
    j = p-1
    
    for i in range(p, r) :
        if A[i] <= A[r] :
            j += 1
            if i != j :
                Ai = A[i]
                A[i] = A[j]
                A[j] = Ai
            k += 1
            
            if k == K :
                result = f"{A[j]} {A[i]}"
    
    j += 1 ## 첫 번째로 큰 값의 인덱스(파티션)
    
    if j != r :
        Aj = A[j]
        A[j] = A[r]
        A[r] = Aj
        k += 1
        
        if k == K :
            result = f"{A[j]} {A[r]}"

    if result != None :
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

if result == None :
    print(-1)
else :
    print(result)
    
# 9 10 1 4 5 8 7 3 2 6