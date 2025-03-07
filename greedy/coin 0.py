## 총 N종류의 동전, 각각의 동전을 매우 많이 가지고 있음
## 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 함
## 동전 개수의 최소값은?

from sys import stdin

N, K = map(int, stdin.readline().split())
A = [0 for _ in range(N)]

for i in range(N) :
    A[i] = int(stdin.readline().rstrip())
    
## 쉬움, 그냥 가장 큰 애부터 하나씩 빼보고, 빼지면 거기부터 시작하는 식으로 하면 될듯?
coin_usage = 0

for i in range(N) :
    current_coin = A[N-1-i]
    
    if K >= current_coin :
        coin_usage += K//current_coin
        K = K%current_coin
        
print(coin_usage)