## 2차원 평면 위의 점 N개
## x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬

# from sys import stdin

# N = int(stdin.readline().rstrip())
# coordinate_dict = {}

# for _ in range(N) :
#     x, y = map(int, stdin.readline().split())
    
#     if x in coordinate_dict.keys() :
#         coordinate_dict[x] = coordinate_dict[x] + [y]
    
#     else :
#         coordinate_dict[x] = [y]

# for k in coordinate_dict.keys() :
#     coordinate_dict[k] = sorted(coordinate_dict[k])

# sorted_x = sorted(coordinate_dict.keys())

# string_list = []

# for k in sorted_x :
#     for y in coordinate_dict[k] :
#         string_list.append(str(k) + " " + str(y))

# print("\n".join(string_list))


## 시간초과 뜸
from sys import stdin

N = int(stdin.readline().rstrip())
coordinate_list = [[0, 0] for _ in range(N)]

for i in range(N) :
    coordinate_list[i] = list(map(int, stdin.readline().split()))

coordinate_list.sort()


print("\n".join([str(l[0]) + " " + str(l[1]) for l in coordinate_list]))