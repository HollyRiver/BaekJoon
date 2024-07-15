from sys import stdin

for i in range(2**32) :
    lst = stdin.readline().rstrip()

    if int(lst) == 0 :
        break
    
    rev = ""
    
    for i in range(len(lst)) :
        rev = lst[i] + rev
    
    if int(rev) == int(lst) :
        print("yes")
    else :
        print("no")
        
        
##----------------------------

n, m = map(int, input().split())

lst_n = []
lst_m = []

for i in range(1, 5001) :
    if n%i == 0 :
        lst_n.append(i)

for i in range(1, 5001) :
    if m%i == 0 :
        lst_m.append(i)

if lst_n[-1] != n :
    lst_n.append(n)
if lst_m[-1] != m :
    lst_m.append(m)
    
        
len_n = len(lst_n)
len_m = len(lst_m)
    
times_lst_n = [0]*len_m
times_lst_m = [0]*len_n
    
for i in range(len_n) :
    times_lst_m[i] = lst_n[i]*m
for i in range(len_m) :
    times_lst_n[i] = lst_m[i]*n
        
lst_n.sort(reverse = True)
lst_m.sort(reverse = True)

maximum_common = 1
found_value = False

lst_n
lst_m

for i in range(len_n) :
    if found_value :
        found_value = False
        break
    
    for j in range(len_m) :
        if lst_n[i] == lst_m[j] :
            maximum_common = lst_n[i]
            found_value = True
            break

minimum_common = n*m


for i in range(len_m) :
    if found_value :
        break
    
    for j in range(len_n) :
        if times_lst_n[i] == times_lst_m[j] :
            minimum_common = times_lst_n[i]
            found_value = True
            break

print(maximum_common)
print(minimum_common)