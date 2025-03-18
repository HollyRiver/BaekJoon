## K개의 랜선을 가지고 있음
## 랜선의 길이는 제각각, 모두 같은 길이의 랜선으로 만들고 싶음
## 기존 K개의 랜선으로 N개의 랜선을 제작
## 만들 수 있는 최대 랜선의 길이를 구하는 프로그램

from sys import stdin

K, N = map(int, stdin.readline().split())
cable_lnth = [0 for _ in range(K)]

for i in range(K) :
    cable_lnth[i] = int(stdin.readline().rstrip())
    
## 이거 어떻게 해야 함??? 브루트 포싱은 일단 에바임
## 먼저 가장 짧은 선의 길이로 전체를 나눠봄

cable_lnth.sort()

## 총 몇개의 케이블이 나오는지를 산출하는 함수
def searching(lnth) :
    total_quant = 0
    
    for l in cable_lnth :
        total_quant += l//lnth

    return total_quant

def binary_searching(before_lnth1, before_lnth2) :
    ## 무조건 b1이 더 크고, b2가 더 작아야 함
    after_lnth = before_lnth2 + (before_lnth1 - before_lnth2)//2
    
    if after_lnth == before_lnth1 :
        return "T", after_lnth
    elif after_lnth == before_lnth2 :
        return after_lnth, "T"
    
    total = searching(after_lnth)
    
    if total >= N :
        return before_lnth1, after_lnth
    
    else :
        return after_lnth, before_lnth2
    
maximum_lnth = max(cable_lnth)
total = searching(maximum_lnth)

## K <= N 이므로, 바로 산출해도 됨 -> 안됨
if total >= N :
    print(maximum_lnth)
    
else :
    b1, b2 = binary_searching(maximum_lnth, 0)
    
    for i in range(100) :
        b1, b2 = binary_searching(b1, b2)
    
        if b1 == "T" :
            print(b2)
            
            break
        elif b2 == "T" :
            print(b1)
            
            break
        
        
## 파이썬에서 1 == True, 0 == False를 하면 True가 찍힌다는 것을 알아야 함.