from sys import stdin

N = int(stdin.readline().rstrip())

s = 0

for _ in range(N) :
    txt = stdin.readline().rstrip()
    
    ts = [txt[0]]
    pre_t = txt[0]
    grup = True

    for t in txt[1:] :
        if pre_t != t :
            if t in ts :
                grup = False
                break
            
            else :
                ts.append(t)
                pre_t = t
                
    s += grup*1
    
print(s)