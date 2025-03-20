## 정규분포로 근사 후, 적분 함수를 만들어 계산 가능? -> 절대오차를 10**(-6)까지 줄이려면 정규근사 X
from math import log, comb, exp
from sys import stdin

n, p, Q = map(float, stdin.readline().split())
n = int(n)
Q = int(Q)

lst = [[0]*2]*Q

for i in range(Q) :
    lst[i] = list(map(int, stdin.readline().split()))

def binomial_dist(x, n, p) :
    log_Px = log(comb(n, x)) + x*log(p) + (n-x)*log(1-p)
    return log_Px

## 미리 모든 경우를 계산해두고, 이중 리스트에 정리
## 요청을 받으면 적절한 인덱스로 변환하여 출력

## O(N^2) DP로 처리
## 히스토그램은 증가하다가 감소하는 형태임
## 평균 n*p에서 최대. 평균을 기준으로 한쪽으로 쏠려있는 경우라면, 기준값을 이용해서 연쇄적으로 구할 수 있음

## 확률값이 최대인 x를 기준으로 앞뒤 1200개씩을 최대 범위로 설정하자. -> 좀 줄일 수 있음. 한 1150 근처...
mu = n*p

## p == 0.5인 경우 확률 최대값이 두 개가 나옴
if mu%1 > 0.0 :
    max_quantile = int(mu) + (binomial_dist(int(mu//1), n, p) < binomial_dist(int(mu//1)+1, n, p))

else :
    max_quantile = int(mu) ## 동일한 경우에도 더 작은 x값을 max_quantile로 사용함

minimum_value = max([0, max_quantile - 1200])
maximum_value = min([n, max_quantile + 1200])
searching_len = maximum_value - minimum_value ## O(n**2) 탐색
box_top = [[i for _ in range(searching_len - i)] for i in range(searching_len)]

## 미리 최대 2400개의 확률값을 계산
log_binom_pdf = [binomial_dist(i, n, p) for i in range(minimum_value, maximum_value)] ## 정렬 후, 인덱스를 저장해둬야 할듯

## 1. 주어진 범위가 최고점을 기준으로 한쪽에 쏠려있는 경우
### A. 최고점 아래 범위

## 인덱스는 1차원 인덱스는 그대로, 2차원 인덱스는 i+j로 관리하면 됨
for i in range(searching_len) :
    ## 0번째는 초기값으로 이미 할당되어 있음 : i == j일 때는 경우의 수가 하나임
    for j in range(1, searching_len - i) :
        ## 증가만 할 때 : log_binom_pdf[box_top[i][j]] + log(i+j-box_top[i][j]+1)
        if i + j <= max_quantile :
            previous = box_top[i][j-1]
            box_top[i][j] = previous + ((log_binom_pdf[previous] + log(i+j-previous+1)) <= (log_binom_pdf[previous+1] + log(i+j-previous))) ## 끝점까지의 거리 + 한칸
        ## 감소만 할 때 : log_binom_pdf[box_top[i][j]] + log(box_top[i][j]-i+1)
        elif i >= max_quantile :
            ## 만약 늘렸을 때 더 작아지는 경우 : 이전 값의 음수로 인덱스 이전, 해당 루프 종료, 결과 산출 시 예외처리 필요
            if (log_binom_pdf[i+j-1] + log(j)) > (log_binom_pdf[i+j] + log(j+1)) :
                box_top[i][j:] = [-j+1]*(len(box_top[i]) - j)
                break
            ## 통상적인 상황. 해당 x값 그 자체에서 최대
            else :
                box_top[i][j] = i+j
                
        ## 최고점을 포함하는 경우
        else :
            previous = box_top[i][j-1]
            ## 다음 점의 확률이 기존 확률값 f(x+1)보다 높거나 같은 경우 : 증가만 할 때와 유사
            if log_binom_pdf[previous+1] <= log_binom_pdf[i+j] :
                box_top[i][j] = previous + ((log_binom_pdf[previous] + log(i+j-previous+1)) <= (log_binom_pdf[previous+1] + log(i+j-previous)))
            ## 다음 점의 확률이 기존 확률값 f(x)보다 높고, f(x+1)보단 낮은 경우 : 기점.
            elif log_binom_pdf[previous] < log_binom_pdf[i+j] :
                ## 여기서 기존 확률값을 유지하거나, i+j로 점프하는 것이 가능해짐.
                ## 기존 박스보다 새로운 박스가 더 크거나 같은 경우
                if (log_binom_pdf[previous] + log(i+j-previous+1)) <= (log_binom_pdf[i+j] + log(i+j-previous)) :
                    box_top[i][j] = i+j ## 좌측 영역이 i에서 더 멀어짐. (i+j) - (previous+1) + 1이 너비가 됨 -> 적절한 처치 필요함 : 정렬을 잘 이용하면 될 것 같은데...
                else :
                    box_top[i][j] = previous ## 기존 확률값 유지 : 다음으로 결정 이전
                    
                
                
            ## 다음 점의 확률이 기존 확률값보다 낮은 경우 : 적어도 한 쪽 끝단은 무조건 닿아야 유의미함. 그렇지 않다면 전역 최대값에 해당. 조건으로 넓이를 처리할 수 있음... 아마도.
            ## 좌측 영역에서 떠있을 수 있음. 만약 좌측 영역의 값이 전역 최소값의 좌측 끝단보다 작다면, 사실상 좌측 끝단과 동일한 판정을 받음.
            ## 좌측 영역에서 떠있는 경우, j가 증가함에 따라 좌측 영역도 증가할 수 있음.
            
            ## i가 끝단에 닿아있고, i+j에서 인덱스 변화가 없으면, 루프 종료 후 이후 값은 음수로 처리.
            
            if 
            

box_size = []