from sys import stdin

T = int(stdin.readline().rstrip())
dp = [1, 1, 1, 2, 2] + [None for _ in range(95)]

for i in range(5, 100) :
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(T) :
    N = int(stdin.readline().rstrip())
    print(dp[N-1])