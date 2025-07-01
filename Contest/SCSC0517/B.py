N = int(input())

max_floor_dict = [20]
max_floor_dict = max_floor_dict + [18*2 + 15*(i-2) + 11 + 6*2*(i-2) for i in range(2, 2026)]

min_floor_dict = [15]
min_floor_dict = min_floor_dict + [10*2 + 6*(i-2) + 3 + 1*2*(i-2) for i in range(2, 2026)]


print(sum(max_floor_dict[:N]) + sum(min_floor_dict[:N]))