# 듣잡 N, 보잡 M

from sys import stdin

N, M = map(int, stdin.readline().split())

dj = set()
bj = set()

for i in range(N) :
    dj.add(stdin.readline().rstrip())

for j in range(M) :
    bj.add(stdin.readline().rstrip())
    
dbj = sorted(dj & bj)

print(len(dbj))

for m in dbj :
    print(m)