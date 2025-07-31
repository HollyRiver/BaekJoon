from sys import stdin

W = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

## 전부 다 작은 인덱스를 가리키고, 직전 인덱스만 가리키므로 간단하게 가능
for i in range(1, 21) :
    for j in range(1, 21) :
        for k in range(1, 21) :
            W[i][j][k] = W[i-1][j][k] + W[i-1][j-1][k] + W[i-1][j][k-1] - W[i-1][j-1][k-1]

for _ in range(2**32) :
    a, b, c = map(int, stdin.readline().split())
    
    if a == -1 and b == -1 and c == -1 :
        break
    
    if a <= 0 or b <= 0 or c <= 0 :
        print(f"w({a}, {b}, {c}) = 1")
    elif a > 20 or b > 20 or c > 20 :
        print(f"w({a}, {b}, {c}) = {W[20][20][20]}")
    else :
        print(f"w({a}, {b}, {c}) = {W[a][b][c]}")