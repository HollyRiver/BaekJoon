lst = [2]*16

for i in range(1, 16) :
    lst[i] = lst[i-1]*2-1


print(lst[int(input())]**2)