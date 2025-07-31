from sys import stdin

txt = stdin.readline().strip()

S = [txt[0]]

for t in txt[1:] :
    if (t == ")" and S[-1] == "(") :
        S[-1] = "|"
    
    else :
        S.append(t)
        
layer = 0
sticks = 0
        
for e in S[::-1] :
    if e == ")" :
        layer += 1
        sticks += 1
    elif e == "|" :
        sticks += layer
    else :
        layer -= 1
        
print(sticks)