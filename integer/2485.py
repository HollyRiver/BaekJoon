## 입력된 거리의 최대공약수를 구해서 그만큼 심어야 함
## 입력 될 때마다 갱신, 심은 나무의 수를 추가
## 최대공약수 값이 변경되면 이전 범위의 나무도 다시 심어야 함
from sys import stdin

N = int(stdin.readline().rstrip())

## 초기값 설정
a = int(stdin.readline().rstrip())
b = int(stdin.readline().rstrip())

distance = b-a
curr_trees = 2

for _ in range(2, N) :
    a = b
    b = int(stdin.readline().rstrip())
    
    new_dist = b-a
    
    if new_dist == distance :
        curr_trees += 1
    else :    
        lnths = [distance, new_dist]
        lnths.sort(reverse = True)
        
        for _ in range(2**16) :
            R = lnths[0]%lnths[1]
            
            if R == 0 :
                curr_trees += (distance//lnths[1] - 1)*(curr_trees-1) + (new_dist//lnths[1])
                distance = lnths[1] ## 갱신
                break
            else :
                lnths = [lnths[1], R]

print(curr_trees - N)