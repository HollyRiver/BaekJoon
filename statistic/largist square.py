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

## Binom(4000, 0.5) 기준으로 대충 1800선까지 0으로 없는 셈 쳐도 오차에 문제가 없음.
## Binom(1000, 0.5) 기준으로 대충 400선까지 0으로 없는 셈 쳐도 오차에 문제가 없음.
## Binom(200, 0.5) 기준으로 대충 60선까지 0으로 없는 셈 쳐도 오차에 문제가 없음.

## 미리 모든 경우를 계산해두고, 이중 딕셔너리에 정리
## 요청을 받으면 딕셔너리에서 빼와서 사용함

## O(N^2) DP로 처리
## 히스토그램은 증가하다가 감소하는 형태임
## 평균 n*p에서 최대. 평균을 기준으로 한쪽으로 쏠려있는 경우라면, 기준값을 이용해서 연쇄적으로 구할 수 있음

## 확률값이 최대인 x를 기준으로 앞뒤 1200개씩을 최대 범위로 설정하자.
mu = n*p

if mu%1 > 0.0 :
    max_quantile = int(mu//1) + (binomial_dist(int(mu//1), n, p) < binomial_dist(int(mu//1)+1, n, p))

else :
    max_quantile = int(mu)

minimum_value = max([0, max_quantile - 1200])
maximum_value = min([n, max_quantile + 1200])
searching_len = maximum_value - minimum_value ## O(n**2) 탐색
box_top = [[i for _ in range(searching_len - i)] for i in range(searching_len)]

## 미리 최대 2400개의 확률값을 계산
log_binom_pdf = [binomial_dist(i, n, p) for i in range(minimum_value, maximum_value)]

## 1. 주어진 범위가 최고점을 기준으로 한쪽에 쏠려있는 경우
### A. 최고점 아래 범위

## 인덱스는 1차원 인덱스는 그대로, 2차원 인덱스는 i+j로 관리하면 됨
for i in range(searching_len) :
    ## 0번째는 초기값으로 이미 할당되어 있음 : i == j일 때는 경우의 수가 하나임
    for j in range(1, searching_len - i) :
        ## 증가만 할 때
        if i + j <= max_quantile :
            previous = box_top[i][j-1]
            box_top[i][j] = previous + ((log_binom_pdf[previous] + log(i+j-previous+1)) <= (log_binom_pdf[previous+1] + log(i+j-previous))) ## 끝점까지의 거리 + 한칸
        ## 감소만 할 때
        elif i >= max_quantile :
            ## 만약 늘렸을 때 더 작아지는 경우 : 이후 출력 고정, 해당 루프 종료
            if (log_binom_pdf[i+j-1] + log(j)) > (log_binom_pdf[i+j] + log(j+1)) :
                box_top[i][j:] = [previous]*(len(box_top[i]) - j)
                break
            ## 통상적인 상황. 해당 x값 그 자체에서 최대
            else :
                box_top[i][j] = i+j
                
        ## 평균을 포함하는 경우
        else :
            

box_size = []
