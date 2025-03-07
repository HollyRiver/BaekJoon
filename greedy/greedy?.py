## 갑자기 골드가 훅 들어와버리네
# |f(x) - f(y)| <= L|x-y|를 만족하는 가장 작은 실수 L을 찾음
# N개의 정수 x에 대해서 L을 전부 찾음.

from sys import stdin
from math import log2

## input & formatting
N = int(stdin.readline())
X = [[0, 0.0] for _ in range(N)]

for i in range(N) :
    x, z = stdin.readline().split()
    X[i][0] = int(x)
    X[i][1] = float(z)

X_sorted = sorted(X)
beam_size = int(log2(N)) ## 양옆으로 늘릴 사이즈이므로, 엄밀히는 (1+2*log2(N))
Ls = []

for i in range(N) :
    if i <= beam_size :
        beam = X_sorted[0:i+beam_size+1]
    elif i >= N - beam_size :
        beam = X_sorted[i-beam_size:]
    else :
        beam = X_sorted[i-beam_size:i+beam_size+1]
    
    for b in beam :
        if (X_sorted[i][0] != b[0]) :
            Ls.append(abs(X_sorted[i][1] - b[1])/abs(X_sorted[i][0] - b[0]))
        
print(max(Ls))