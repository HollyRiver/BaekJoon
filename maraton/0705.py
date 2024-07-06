A, B, C = map(int, input().split())

spec = B/A

print(C*spec*3)


import math
square_metres = int(input())

print(math.sqrt(square_metres/math.pi)*2*math.pi)

lenth = int(input())
final_output = ""

for i in range(lenth) :
    n = int(input())
    
    output = "#"*n + "\n"
    
    if n > 2 :
        for j in range(n-2) :
            output = output + f"#{'J'*(n-2)}#\n"
            
    if n != 1 :
        output = output + "#"*n
    else :
        output = output[:-1]
    final_output = final_output + output + "\n\n"

print(final_output[:-2])

##-----------------

N = int(input())

line = "@"*N + "\n"
block = line*N

top = block*4

bottom_line = "@"*N*5+"\n"

bottom = bottom_line*N

output = top+bottom

print(output[:-1])

##------------------

N = int(input())

n = N
i = 1
t = 0

for j in range(10**7) :
    if i <= n :
        n -= i
        t += 1
        i += 1

    else :
        i = 1

    if n == 0 :
        break
    
print(t)

##----------------------

n, w = map(int, input().split())
txt = input()

word_group = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"