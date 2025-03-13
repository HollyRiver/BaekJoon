## N장의 카드가 있고, 1부터 N까지의 번호가 붙어 있으며, 오름차순으로 쌓여있다.
## 1. 제일 위에 있는 카드를 바닥에 버린다.
## 2. 제일 위에 있는 카드를 아래로 내린다.
## 상기 과정을 카드가 한 장 남을 때까지 반복했을 때, 마지막에 남는 카드는?

## 파이썬에선 collections 모듈의 deque를 사용
from collections import deque ## Double Ended Queue

N = int(input())

deck = deque([i for i in range(1, N+1)])

for i in range(2*N-3) :
    if i%2 == 0 :
        deck.popleft()
        
    else :
        deck.append(deck.popleft())
        
print(deck[0])