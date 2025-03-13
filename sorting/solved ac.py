## 어떤 문제의 난이도는 그 문제를 푼 사람들이 제출한 난이도 의견으로 결정
## 아직 아무 의견이 없다면 문제의 난이도는 0
## 의견이 하나 이상 있다면, 문제의 난이도는 모든사람의 난이도 의견의 30% 절사평균
## 절사평균 : 가장 큰 값, 가장 작은 값들을 제외하고 평균 산출
## 30% 절사평균 : 위에서 15%, 아래에서 15%를 제외하고 평균 계산
## 제외되는 사람의 수는 위, 아래에서 각각 반올림
## 계산된 평균도 정수로 반올림

from sys import stdin

n = int(stdin.readline().rstrip())

if n > 0 :
    level_list = [0 for _ in range(n)]

    for i in range(n) :
        level_list[i] = int(stdin.readline().rstrip())
        
    level_list.sort()
    lnth = len(level_list)
    trimmed = int((lnth*0.15 + 0.5)//1)

    trimmed_list = level_list[trimmed:lnth-trimmed]
    
    # print(round(sum(trimmed_list)/len(trimmed_list))) ## banker's rounding
    
    print(int((sum(trimmed_list)/len(trimmed_list) + 0.5)//1))
    
else :
    print(0)