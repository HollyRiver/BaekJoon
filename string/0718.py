from sys import stdin

N = int(stdin.readline().rstrip())

len_lst = [[] for _ in range(50)]

for i in range(N) :
    value = stdin.readline().rstrip()
    
    if (len_lst[len(value)-1] == []) or (value not in len_lst[len(value)-1]) :
        len_lst[len(value)-1].append(value)

for i in range(50) :
    len_lst[i].sort()
    for j in len_lst[i] :
        print(j)