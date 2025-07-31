from sys import stdin

N = int(stdin.readline().rstrip())
A = list(map(int, stdin.readline().split()))
B = stdin.readline().split()
M = int(stdin.readline().rstrip())
C = stdin.readline().split()

if sum(A) == N :
    result = C ## 전부 스택인 경우
else :
    Q = [b for a, b in zip(A[::-1], B[::-1]) if a == 0]
    start = 0
    result = []
    
    for c in C :
        Q.append(c)
        result.append(Q[start])
        start += 1
        
print(" ".join(result))

## 스택이면 그대로 빼고, 큐면 기존 거 빼고
## 사실상 스택은 패스해도 되고, 큐만 고려하면 됨