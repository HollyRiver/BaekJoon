from sys import stdin
from random import randint

N, Q = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

for _ in range(Q) :
    q = list(map(int, stdin.readline().split()))
    
    if q[0] == 1 :
        i, j, k = q[1:]
        k -= 1 ## 0번부터
        B = A[i-1:j] ## i-1부터 j-1까지
        a = 0
        b = len(B)-1
        
        while a != b :
            p = randint(a, b) ## 리스트 원소 중 하나
            
            ## swap
            Bp = B[p]
            B[p] = B[b]
            B[b] = Bp
            
            l = a
            
            for m in range(a, b) :
                if B[m] <= Bp :
                    if m != l :
                        Bm = B[m]
                        B[m] = B[l]
                        B[l] = Bm
                    l += 1
            
            B[b] = B[l]
            B[l] = Bp ## B[b]
            
            if l == k :
                break
            elif l > k :
                b = l-1
            else :
                a = l+1
                
        print(B[k])
    
    else :
        i, j = q[1:]
        i -= 1
        j -= 1
        Ai = A[i]
        A[i] = A[j]
        A[j] = Ai

## legacy : 오류 있음

for _ in range(Q) :
    q = list(map(int, stdin.readline().split()))
    
    if q[0] == 1 :
        i, j, k = q[1:]
        k -= 1
        B = A[i-1:j] ## 1부터 시작
        a = 0
        b = j-i
        
        print(B)
        
        while a != b :
            ## random pivot
            p = randint(a, b)
            
            ## swap
            Bp = B[p]
            B[p] = B[b]
            B[b] = Bp
            i = 0
            
            ## a to b-1
            for j in range(a, b) :
                if B[j] <= B[b] :
                    if i != j :
                        Bi = B[i]
                        B[i] = B[j]
                        B[j] = Bi
                    i += 1
            
            if i != b :
                Bi = B[i]
                B[i] = B[b]
                B[b] = Bi
                
            if i == k :
                break
            elif i > k :
                b = i-1
            else :
                a = i+1
        
        print(B[i])
        
    else :
        i, j = q[1:]
        i -= 1
        j -= 1
        Ai = A[i]
        A[i] = A[j]
        A[j] = Ai
        


## 원소의 총 개수가 5개 이하이면 k번째 원소를 찾고 끝
##---##
## 전체 원소를 5개씩의 원소를 가진 n/5개의 그룹으로 나눔
## 각 그룹에서 중앙값을 찾음 -> 원소가 짝수개이면 두개 중 임의로 선택
## 그룹별 중앙값들의 중앙값을 재귀적으로 계산 -> Median to Medians
## 뭔가 잘못됨, 랜덤피벗에 영향을 크게 받음