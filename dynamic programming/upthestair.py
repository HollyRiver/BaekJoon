## 계단 꼭대기에 위치한 도착점까지 가는 게임
## 한 번에 한 계단/두 계단 씩 오르고 있음
## 연속된 세 개의 계단을 모두 밟아서는 안됨
## 마지막 도착계단은 반드시 밟아야 함

## 계단의 개수는 300개 이하, 점수는 10000점 이하

from sys import stdin

N = int(stdin.readline().rstrip())
score_list = [0 for _ in range(N)]

for i in range(N) :
    score_list[i] = int(stdin.readline().rstrip())
    
## 어떻게 할 수 있을까?
## 일단 최대한 많이 밟는 것이 중요함. 뛰어넘지 않는 게 좋음.
## 두 개씩 밟고, 하나를 뛰어넘는 것이 이상적임
## 두 개를 밟았을 때, 그 다음 칸의 점수가 두 칸을 밟았을 때보다 적다면, 손해임

## 현재 칸이 다음 칸보다 점수가 높으면 진행 -> 다음은 무조건 점프해야함
## 현재 칸보다 다음 칸이 점수가 높으면 점프 -> 한칸은 패스하고 처음 상태로 복귀

## 초기 상태 : 점프도 안하고, 두 칸 연속으로 가지도 않은 상태
summation = 0

if N >= 7 :
    ## 첫 칸은 무조건 밟음
    summation += score_list[0]
    jumping = False ## 발이 땅에 닿은 상태
    proceed = False ## 연속으로 가지 않은 상태
    
    for i in range(1, N-5) :
        if (not jumping) and (not proceed) :
            ## 현재 칸이 다음 칸보다 점수가 높으면 진행
            if score_list[i] >= score_list[i+1] :
                proceed = True
                summation += score_list[i]
            ## 현재 칸이 다음 칸보다 점수가 낮으면 다음칸으로 점프, 카운트하지 않음
            else :
                jumping = True
            
        ## 연속으로 진행한 상태, 해당 칸은 무조건 뛰어야 함
        elif proceed :
            proceed = False
            jumping = True ## 연속 두 칸을 밟았으므로 무조건 점프
        
        ## 점프와 진행이 동시에 일어날 수 없으므로 나머지는 점프
        else :
            summation += score_list[i] ## 해당 칸은 무조건 밟아야 함
            jumping = False ## 땅에 다시 닿음, 처음으로 돌아감
            
    ## 직전 상태가 초기 -> 무조건 세 번 밟음
    last_list = score_list[N-5:]

    if (not jumping) and (not proceed) :
        a = last_list[1] + last_list[2] + last_list[4]
        b = last_list[0] + last_list[2] + last_list[4]
        c = last_list[1] + last_list[3] + last_list[4]
        
        summation += max([a, b, c])
        
    ## 직전 상태가 진행 -> 무조건 세 번 밟음
    elif proceed :
        a = last_list[1] + last_list[2] + last_list[4]
        b = last_list[1] + last_list[3] + last_list[4]
        
        summation += max([a, b])
        
    ## 직전 상태가 점프 -> 세번 또는 네번 밟을 수 있음
    else :
        a = last_list[0] + last_list[2] + last_list[4]
        b = sum(last_list) - last_list[2]

        summation += max([a, b])

## 적은 경우는 브루트 포싱
else :
    setting = []
    
    for i in range(2**(N-2), 2**(N-1)) :
        candidate = list(bin(i)[2:] + "1")
        
        for j in range(N-2) :
            if sum([int(k) for k in candidate[j:j+3]]) >= 3 :
                filtered = True
            
        for j in range(N-1) :
            if sum([int(k) for k in candidate[j:j+2]]) == 0 :
                filtered = True
            
        if filtered :
            filtered = False
        else : 
            setting.append(candidate)
    
    scoring = []
    
    for s in setting :
        scoring.append(sum([score_list[i] for i in range(N) if s[i] == '1']))
    
    summation += max(scoring)
        

print(summation)