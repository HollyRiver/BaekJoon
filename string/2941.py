c_alpha = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
c_alpha_start = ["c", "d", "l", "n", "s", "z"]

txt = input()

i = 0
lnth = 0

for _ in range(len(txt)) :    
    if txt[i] in c_alpha_start :
        if txt[i:i+2] in c_alpha :
            i += 2
        elif txt[i:i+3] == "dz=" :
            i += 3
        else :
            i += 1
    
    else :
        i += 1
    
    lnth += 1
    
    if i >= len(txt) :
        break
    
print(lnth)