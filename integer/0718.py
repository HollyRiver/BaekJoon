from sys import stdin
import gc

N = int(stdin.readline().rstrip())

lst = [0 for _ in range(10000)]

for i in range(N) :
    value = int(stdin.readline().rstrip())
    lst[value-1] = lst[value-1] + 1

del N
del value
gc.collect()

for i in range(10000) :
    if lst[i] != 0 :
        print(((str(i+1) + "\n")*lst[i])[:-1])
        
        
        
from sys import stdin

N = int(stdin.readline().rstrip())

lst = [0]*10000

for i in range(N) :
    value = int(stdin.readline().rstrip())
    lst[value-1] = lst[value-1] + 1

for i in range(10000) :
    if lst[i] != 0 :
        print(((str(i+1) + "\n")*lst[i])[:-1])

        
##-------------------------------------

N, K = map(int, input().split())

numerator = 1
denominator = 1

for i in range(K) :
    numerator *= N-i
    
for j in range(K) :
    denominator *= j+1
    
print(int(numerator/denominator))

##--------------------------------------

a = input()
b = input()
c = input()

input_lst = [a, b, c]

is_int = [None, None, None]

try :
    a = int(a)
    is_int[0] = True
    
except :
    is_int[0] = False
    pass
    
try :
    b = int(b)
    is_int[1] = True
    
except :
    is_int[1] = False
    pass

try :    
    c = int(c)
    is_int[2] = True
    
except :
    is_int[2] = False
    pass

ind = [i for i in range(3) if is_int[i]][-1]

output_num = input_lst[ind] + (3-ind)

if output_num%3 == 0 :
    if output_num%5 == 0 :
        print("FizzBuzz")
    else :
        print("Fizz")
elif output_num%5 == 0 :
    print("Buzz")
else :
    print(output_num)
    
##-----------------------------------------

N = int(input())

lst = [666]

for i in range(1, 1000) :
    lst.append(int(str(i)+"666"))
    for j in list(range(1, 1000)) + ["0"] + ["000"] + ["0" + str(k) for k in range(100)] :
        lst.append(int(str(i)+"666"+str(j)))

for j in list(range(1, 1000)) + ["0"] + ["000"] + ["0" + str(k) for k in range(100)] :
    lst.append(int("666"+str(j)))
        
lst = list(set(lst))
lst.sort()

lst[499]


N = int(input())

lst = [666]

for i in range(1, 1000) :
    lst.append(int(str(i)+"666"))
    for j in list(range(1, 1000)) + ["0"] + ["000"] + ["0" + str(k) for k in range(100)] :
        lst.append(int(str(i)+"666"+str(j)))

for j in list(range(1, 1000)) + ["0"] + ["000"] + ["0" + str(k) for k in range(100)] :
    lst.append(int("666"+str(j)))
        
lst = list(set(lst))
lst.sort()

lst[N-1]


N = int(input())

lst = [666]

for i in range(1, 1000) :
    lst.append(int(str(i)+"666"))
    for j in list(range(1, 1000)) + ["0"] + ["000"] + ["0" + str(k) for k in range(100)] :
        lst.append(int(str(i)+"666"+str(j)))

for j in list(range(1, 1000)) + ["0"] + ["000"] + ["0" + str(k) for k in range(100)] :
    lst.append(int("666"+str(j)))
        
lst = list(set(lst))
lst.sort()

lst[N-1]

## 재귀로 푸는게 속 편할듯

N = int(input())

lst = [666]

def inserting(first_len = 0) :
    if first_len == 0 :
        for i in list(range(10000)) + ["0"*(i+1) for i in range(4)] + ["0" + str(k) for k in range(10**(3))] :
            lst.append(int("666"+str(i)))
            
        inserting(first_len = 1)
    elif first_len < 4 :
        for i in range(10**(first_len-1), 10**first_len) :
            lst.append(int(str(i)+"666"))
            for j in list(range(10**(4-first_len))) + ["0"*(i+1) for i in range(4-first_len)] + ["0" + str(k) for k in range(10**(3-first_len)) if first_len != 0] :
                lst.append(int(str(i)+"666"+str(j)))
                
        inserting(first_len = first_len + 1)
        
    else :
        for i in range(1000, 10**first_len) :
            lst.append(int(str(i)+"666"))
        
inserting()

lst = list(set(lst))
lst.sort()

lst[-1]
print(lst[N-1])

lst[-1]

["0"*(i+1) for i in range(1)]
["0" + str(k) for k in range(10**(value)) if value != 0]
list(range(10**(3)))

list(range(10**1))

1000


lst = []

def inserting():
    for i in range(10000):
        num = str(i)
        if "666" in num:
            lst.append(int(num))
        else:
            for j in range(5 - len(num)):
                lst.append(int(num[:j] + "666" + num[j:]))
                
    lst.sort()
    return lst

lst = inserting()
sorted(list(set(lst)))[-1]


##-------------------------------------------------

N = int(input())

lst = []

for i in range(2700000) :
    if "666" in str(i) :
        lst.append(i)
        
print(lst[N-1])