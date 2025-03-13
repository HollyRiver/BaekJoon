## 잘못된 수를 부를 때마다 0를 외쳐서, 가장 최근에 쓴 수를 지우게 한다.
## 모든 수를 받아 적은 후, 그 수의 합을 알고 싶다.
## 정수가 0일 경우에 지울 수 있는 수가 있음을 보장할 수 있음.

from sys import stdin

K = int(stdin.readline().rstrip())
integr_stack = [0]

for i in range(K) :
    N = int(stdin.readline().rstrip())
    
    if N == 0 :
        del integr_stack[-1]
        
    else :
        integr_stack.append(N)
        
print(sum(integr_stack))