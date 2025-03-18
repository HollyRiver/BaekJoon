## 여러 개의 문서가 쌓이면 큐에 쌓여 선입선출
## 현재 큐의 가장 앞에 있는 문서의 중요도 확인
## 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있으면
## 현재 문서를 가장 뒤에 재배치

## 현재 큐에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇번째로 인쇄되는지

from collections import deque
from sys import stdin

T = int(stdin.readline().rstrip())

printing = ["" for _ in range(T)]

for i in range(T) :
    N, M = map(int, stdin.readline().split())
    
    importancy = deque(map(int, stdin.readline().split()))
    
    ordering = 0
    
    for _ in range(N**2) :
        if M > 0 :
            if importancy[0] < max(importancy) :
                importancy.append(importancy.popleft())
                
            else :
                del importancy[0]
                
                ordering += 1
            
            M -= 1
        
        else :
            if importancy[0] < max(importancy) :
                importancy.append(importancy.popleft())
            
                M = len(importancy) - 1
                
            else :
                printing[i] = str(ordering+1)
                break
            
print("\n".join(printing))