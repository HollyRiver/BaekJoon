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


##-------------------

from sys import stdin

T = int(stdin.readline().rstrip())

fst_floor = [0]*14
snd_floor = [0]*14

residents_lst = [[0,0]]*T

for t in range(T) :
    residents_lst[t] = [int(stdin.readline().rstrip()), int(stdin.readline().rstrip())]

residents_lst.sort()
switch = False
residents = 0
k = 0
n = 0

for t in range(T) :
    k_ = k
    n_ = n
    k, n = residents_lst[t]
    
    if k_ != k :
        if switch :
            fst_floor = [0]*14
        else :
            snd_floor = [0]*14
        switch = not switch
    
    if k == 1 :
        residents = (n+1)*n/2
        print(residents)
        zero_default[n] = residents
    else :
        residents = sum(zero_default[:n])
        print(residents)
        pre_residents[n] = residents