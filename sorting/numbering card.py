## 숫자 카드는 정수 하나가 적혀져 있는 카드이다.
## N개의 숫자 카드를 가지고 있음
## 정수 M개에 대하여 이 수가 적혀있는 숫자 카드를 몇개 가지고 있는지 산출

from sys import stdin

N = int(stdin.readline().rstrip())
holding_set = list(map(int, stdin.readline().split()))

M = int(stdin.readline().rstrip())
searching_set = list(map(int, stdin.readline().split()))

holding_set.sort()
counting_dict = {}

pre_num = -1e8

for n in holding_set :
    if n > pre_num :
        counting_dict[n] = 1
        pre_num = n
    else :
        counting_dict[n] += 1

for n in searching_set :
    if n not in counting_dict.keys() :
        counting_dict[n] = 0

print(" ".join([str(counting_dict[n]) for n in searching_set]))