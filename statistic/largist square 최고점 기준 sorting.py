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
maximum_value = min([n+1, max_quantile + 1200])
searching_len = maximum_value - minimum_value ## O(n**2) 탐색, n은 최대가 2400

## 미리 최대 2400개의 확률값을 계산
log_binom_pdf = [binomial_dist(i, n, p) for i in range(minimum_value, maximum_value)] ## 부분적으로 정렬을 수행해야 할 수 있음.

## i~max_quantile 최초 sorting. 이후 마지막 원소(가장 작은 값)부터 하나씩 제거하며 범위 산출
fromi_tomax_pdf = sorted(log_binom_pdf[:max_quantile+1], reverse = True)

## 인덱스는 1차원 인덱스는 그대로, 2차원 인덱스는 i+j로 관리하면 됨
log_box_size = [[0.0 for _ in range(searching_len - i)] for i in range(searching_len)] ## 0번째 원소의 길이는 2400, 2399번째 원소의 길이는 1

## 전역 최대값을 미리 계산
sorted_pdf = sorted(log_binom_pdf, reverse = True)
maximum_area = -1e8
end_stack = 0

for i, log_px in enumerate(sorted_pdf) :
    current_area = log_px + log(i+1)
    
    if current_area >= maximum_area :
        maximum_area = current_area ## 스칼라이므로 얕은복사
        end_stack = 0
    else :
        end_stack += 1
        
        ## p = 0.5인 경우 등의 이유로 같은 확률값이 존재할 수 있음.
        if end_stack >= 2 :
            current_px = log_px
            break

lower = None
upper = None

for i, px in enumerate(log_binom_pdf) :
    if lower == None :
        if px >= current_px :
            lower = i
    else :
        if px == current_px :
            upper = i
            break
        elif px < current_px :
            upper = i-1
            break
        
## maximum_area / [lower, upper]가 정의됨. (a <= lower) and (b >= upper)인 경우, 최대 면적은 항상 maximum_area로 고정됨

## 나머지 모든 상횡에서의 최대 면적 계산
for i in range(searching_len) :
    if fromi_tomax_pdf != [] :
        fromi_toj_pdf = fromi_tomax_pdf.copy()  ## 1차원 리스트이므로 copy()를 통해 얕은복사.
    
    ## 각 케이스의 0번째 값은 초기값으로 할당 : a == b이므로 경우의 수가 하나임
    log_box_size[i][0] = log_binom_pdf[i]
    width = 1
    
    for j in range(1, searching_len - i) :
        ## 1. 주어진 범위가 최고점을 기준으로 한쪽에 쏠려있는 경우
        ### A. 최고점 아래 범위 : i+j는 제공된 쿼리에서 upper bound에 해당됨.
        ## 증가만 할 때 : 우측 범위는 무조건 닿아있음
        if i + j <= max_quantile :
            ## a : 확률값 그대로, b : 확률값 좌측에서 한 단계 위로
            a, b = (log_binom_pdf[i+j - width] + log(width+1), log_binom_pdf[i+j+1 - width] + log(width))
            
            ## 너비가 더 넓어짐. 확률값은 그대로임
            if a >= b :
                log_box_size[i][j] = a
                width += 1
            
            ## 너비는 그대로, 확률값은 더 높아짐
            else :
                log_box_size[i][j] = b
        
        ### B. 최고점 위 범위 : 최고점이 두 개일 수 있음. 이 경우 더 작은 x값을 기준으로 택함.
        ## 감소만 할 때 : 좌측 범위는 무조건 닿아있음. 너비는 통상적으로 항상 j+1임
        elif i >= max_quantile :
            ## a : 확률값/너비 그대로, b : 확률값 우측에서 한 단계 아래로/너비 한 칸 증가
            a, b = (log_binom_pdf[i+j-1] + log(j), log_binom_pdf[i+j] + log(j+1))
            
            ## 통상적인 상황.
            if a <= b :
                log_box_size[i][j] = b
                
            ## 늘렸을 때 더 작아지는 경우 : 이전 값의 넓이로 이후 모든 값을 일괄적으로 처리, i번째 루프 종료
            else :
                log_box_size[i][j:] = [log_box_size[i][j-1]]*(len(log_box_size[i]) - j)
                break
                
        ## 2. 주어진 범위가 최고점을 포함하는 경우 : 가용범위에서 확률값 기준으로 정렬하여 탐색
        else :
            ## 최대 면적이 되는 영역을 포함하는 경우. 항상 maximum_area로 고정됨
            if (i <= lower) and (i+j >= upper) :
                log_box_size[i][j:] = [maximum_area]*(len(log_box_size[i]) - j)
                break
                
            else :            
                ## 가용범위. 해당 과정을 거쳐간 이후, 최대 면적이 되는 영역을 포함하게 되므로 정렬 및 원소 삽입은 여기서만
                fromi_toj_pdf.append(log_binom_pdf[i+j]) ## 한 번 sorting해놓고, 추가한 뒤 재정렬
                fromi_toj_pdf.sort(reverse=True)
                
                ## 가용범위에서 최대값을 찾음. 시간복잡도를 결정짓는 부분. width를 지정하고 앞뒤로 탐색하면 중복 탐색을 막을 수 있음 -> 조금 생각이 필요함
                local_max = -1e8
                end_stack = 0
                
                for k, log_px in enumerate(fromi_toj_pdf) :
                    local_current = log_px + log(k+1)
                    
                    if local_current >= local_max :
                        local_max = local_current
                        end_stack = 0
                    else :
                        end_stack += 1
                                           
                        if end_stack >= 2 :
                            break
                    
                ## 범위를 늘려도 넓이가 똑같은 경우 : 이전 값의 넓이로 이후 모든 값을 일괄적으로 처리, i번째 루프 종료 
                if local_max < log_box_size[i][j-1] :
                    log_box_size[i][j:] = [log_box_size[i][j-1]]*(len(log_box_size[i]) - j)
                    break
                
                ## 범위를 늘렸을 때 넓이가 커진 경우 : 해당 넓이로 먹임
                else :
                    log_box_size[i][j] = local_max
    
    ## i가 max_quantile을 넘을 경우, 리스트가 전부 비게 됨.
    if fromi_tomax_pdf != [] :
        del fromi_tomax_pdf[-1] ## 마지막 원소 제거, i+1부터 시작
            
output = [0.0]*Q

for i, bound in enumerate(lst) :
    lower = max([0, (bound[0] - minimum_value)])
    upper = min([searching_len, (bound[1] - minimum_value)])
    
    output[i] = str(exp(log_box_size[lower][upper-lower]))
    
print("\n".join(output))