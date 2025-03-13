## y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순으로 정렬

## 파이썬 개날먹
from sys import stdin

N = int(stdin.readline().rstrip())
coordinate_list = [[0, 0] for _ in range(N)]

for i in range(N) :
    x, y = map(int, stdin.readline().split())
    coordinate_list[i] = [y, x]

coordinate_list.sort()

print("\n".join([str(l[1]) + " " + str(l[0]) for l in coordinate_list]))