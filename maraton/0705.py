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

##----------------------공백을 연속으로 누를 때는 기다릴 필요가 없다.

n, w = map(int, input().split())
txt = list(input())

word_group = {" ":[1,0],
              "A":[2,0], "B":[2,1], "C":[2,2],
              "D":[3,0], "E":[3,1], "F":[3,2],
              "G":[4,0], "H":[4,1], "I":[4,2],
              "J":[5,0], "K":[5,1], "L":[5,2],
              "M":[6,0], "N":[6,1], "O":[6,2],
              "P":[7,0], "Q":[7,1], "R":[7,2], "S":[7,3],
              "T":[8,0], "U":[8,1], "V":[8,2],
              "W":[9,0], "X":[9,1], "Y":[9,2], "Z":[9,3]}

time = 0

for i in range(len(txt)) :
    time += n*(word_group[txt[i]][1]+1)
    
    if (i != 0) & (word_group[txt[i]][0] == word_group[txt[i-1]][0]) & (word_group[txt[i]][0] != 1) :
        time += w

print(time)

txt

##--------------------------

