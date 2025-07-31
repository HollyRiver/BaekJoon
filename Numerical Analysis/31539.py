from sys import stdin

n, b = map(int, stdin.readline().split())

x = [0]*n
y = [0]*n

for i in range(n) :
    x[i], y[i] = map(int, stdin.readline().split())
    

## 로그 최소화랑 동일함

def Sp(a) :
    sp = 0
    
    for xi, yi in zip(x, y) :
        sp += -4*xi*(yi - a*xi - b)**3/n
    
    return sp

if Sp(0) == 0 :
    a = 1
else :
    a = 0

while True :
    sp = Sp(a)
    
    if abs(sp) <= 1e-8 :
        break
    else :
        
        if abs(sp) >= 100 :
            a -= 0.00001*sp
        elif abs(sp) >= 10 :
            a -= 0.001*sp
        else :
            a -= 0.01*sp

print(a) ## 매우 파멸적이다.