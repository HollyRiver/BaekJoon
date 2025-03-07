## 한 대의 ATM에 N명의 사람들이 줄을 서 있음.
## i번째 사람이 돈을 인출하는 데에 걸리는 시간은 P_i분임.
## 사람들이 줄을 서는 순서에 따라 돈을 인출하는 데에 필요한 시간의 합이 달라짐.
## 정확히는 총 소요시간은 똑같지만, 각자 기다리는 시간의 합이 달라짐.
## 오래 걸리는 사람이 가장 나중에 인출하도록 하는 것이 중요함.

## 줄을 서 있는 사람의 수 N과, 인출 시간 P_i가 주어졌을 때, 시간 최소값은?

from sys import stdin

N = int(stdin.readline().rstrip())
Payment_times = list(map(int, stdin.readline().split()))
    
## 정렬하고 합하면 됨
Payment_times.sort(reverse = True)
total_time = 0

for i in range(N) :
    endup = Payment_times.pop()
    total_time += endup*(len(Payment_times)+1)
    
print(total_time)