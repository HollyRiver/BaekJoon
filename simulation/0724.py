payment_lst = list(map(int, input().split()))

lst_arr = []
lst_dep = []

for i in range(3) :
    a, b = map(int, input().split())
    lst_arr[i] = a
    lst_dep[i] = b

lst_arr.sort()
lst_dep.sort()

payment = 0
cars = 0

for i in range(1, 101) :
    for j in range(3) :
        if lst_arr[j] == i :
            cars += 1
        if lst_dep[j] == i :
            cars -= 1
    
    if cars != 0 :
        payment += payment_lst[cars-1]*cars

print(payment)