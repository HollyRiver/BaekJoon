from sys import stdin

n, b = map(int, stdin.readline().split())

x = [0]*n
y = [0]*n

for i in range(n) :
    x[i], y[i] = map(int, stdin.readline().split())
    

def S(a) :
    s = 0
    sp = 0
    
    for xi, yi in zip(x, y) :
        s += (yi - a*xi - b)**3
        sp -= 3*xi*(yi - a*xi - b)**2 ## xi > 0 -> 감소함수
    
    return (-s, -sp) ## 증가함수 형태로 변환

if S(0)[1] == 0 :
    a = 1
else :
    a = 0

while True :
    s, sp = S(a)
    new_a = a - s/sp
    
    if abs(a - new_a) <= 1e-8 :
        break
    else :
        a = new_a
        
print(new_a)