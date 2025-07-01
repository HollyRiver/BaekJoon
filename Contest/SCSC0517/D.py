from sys import stdin

N = int(stdin.readline().rstrip())
train = stdin.readline().rstrip()

top = [1] + [0]*(N-1) + [1]
horizon = [0]*N
bottom = [1] + [0]*(N-1) + [1]

for i, t in enumerate(train[1:N-1]) :
    if t == "2" :
       top[i+2] = 1
       horizon[i+1] = 1
       bottom[i+1] = 1
    elif t == "5" :
        top[i+1] = 1
        horizon[i+1] = 1
        bottom[i+2] = 1
    elif t == "[" :
        top[i+1] = 1
        bottom[i+1] = 1
    else :
        top[i+2] = 1
        bottom[i+2] = 1
    

i = 0
s = 0
    
for _ in range(2**18) :
    if top[i] == top[i+1] :
        if horizon[i] == 1 :
            s += 1
        elif bottom[i] == bottom[i+1] :
            s += 1
        i += 1
    else :
        s += 1
        i += 2
        
    if i >= N :
        break
    
    
i = 0

for _ in range(2**18) :
    if bottom[i] == bottom[i+1] :
        if horizon[i] == 1 :
            s += 1
        i += 1
    else :
        if horizon[i] == 1 :
            s += 1
        elif horizon[i+1] == 1 :
            s += 1
        i += 2
        
    if i >= N :
        break
    
print(s)