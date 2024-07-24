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