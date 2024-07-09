import sys

N = int(input())
numbs = [0]*N

for i in range(N) :
    numbs[i] = int(sys.stdin.readline())
    
print(round(sum(numbs)/N))
print(sorted(numbs)[int((N+1)/2 -1)])

uniq = sorted(list(set(numbs)))
n = len(uniq)
times = [1]*len(uniq)

temp = sorted(numbs)
j = 0

for i in range(N-1) :
    if temp[i+1] == temp[i] :
        times[j] = times[j] + 1
    
    else :
        j += 1

mode_list = sorted([uniq[i] for i in range(n) if times[i] == max(times)])

if len(mode_list) > 1 :
    print(mode_list[1])
else :
    print(mode_list[0])

print(round(max(numbs) - min(numbs)))

##----------------------

x, y = map(int, input().split())

summation = 0

if x == y :
    print(0)

else :
    for i in range(20) :
        if i == 0 :
            summation += 1
            if x+1 == y :
                break
        else :
            if x < y :
                if (i%2 == 1) or (2**i < y-x):
                    summation += 2**i + 2**(i-1)
                elif i%2 == 0 and 2**i >= y-x :
                    summation += 2**(i-1) + y-x
                    break
                
            else :
                if i%2 == 0 or 2**i < x-y:
                    summation += 2**i + 2**(i-1)
                elif i%2 == 1 and 2**i >= x-y :
                    summation += 2**(i-1) + x-y
                    break
                
print(summation)

##----------------

import sys

n, rsq = map(int, input().split())

for i in range(n) :
    map(int, sys.stdin.readline().split())
    
    
##---------------------

from sys import stdin
from math import log, exp, comb

n, p, Q = map(float, stdin.readline().split())
n = int(n)
p = float(p)
Q = int(Q)

# 분포 생성 및 로그로 변환하여 작은 값을 보존
log_probabilities = [log(comb(n, i)) + i * log(p) + (n - i) * log(1 - p) for i in range(n + 1)]

# 누적 합을 미리 계산하여 저장합니다.
cumulative_sum = [0] * (n + 1)
for i in range(1, n + 1):
    cumulative_sum[i] = cumulative_sum[i - 1] + exp(log_probabilities[i])

# 쿼리에 대한 결과를 미리 계산하여 저장합니다.
results = []
for _ in range(int(Q)):
    l, r = map(int, stdin.readline().split())
    min_height = cumulative_sum[l - 1]
    max_area = (cumulative_sum[r] - min_height) * (r - l + 1)
    results.append(max_area)

# 결과를 출력합니다.
print("\n".join(map(str, results)))