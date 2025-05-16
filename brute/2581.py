## 그냥 무지성 브루트 포싱

sosu = [2, 3]

for i in range(5, 10000) :
    is_sosu = True
    
    for s in sosu :
        if i % s == 0 :
            is_sosu = False
            break
        
    if is_sosu :
        sosu.append(i)
        
M = int(input())
N = int(input())

MN_sosu = []

for s in sosu :
    if s >= M and s <= N :
        MN_sosu.append(s)
        
if len(MN_sosu) == 0 :
    print(-1)
else :
    print(sum(MN_sosu))
    print(MN_sosu[0])