from sys import stdin
from math import log, exp, comb

n, p, Q = map(float, stdin.readline().split())
n = int(n)
p = float(p)
Q = int(Q)

# 분포 생성 및 로그로 변환하여 작은 값을 보존
log_probabilities = [log(comb(n, i)) + i * log(p) + (n - i) * log(1 - p) for i in range(n + 1)]

# 누적 합을 미리 계산하여 저장합니다.
cumulative_sum = [0] * (n + 1)
for i in range(1, n + 1):
    cumulative_sum[i] = cumulative_sum[i - 1] + exp(log_probabilities[i])

# 쿼리에 대한 결과를 미리 계산하여 저장합니다.
results = []
for _ in range(int(Q)):
    l, r = map(int, stdin.readline().split())
    min_height = cumulative_sum[l - 1]
    max_area = (cumulative_sum[r] - min_height) * (r - l + 1)
    results.append(max_area)

# 결과를 출력합니다.
print("\n".join(map(str, results)))


##--------------------------------

from sys import stdin
from math import pi, exp, log

def norm_pdf(x, mu, sigma_sq) :
    return 1/(2*pi*sigma_sq)**0.5*exp(-(x-mu)**2/(2*sigma_sq))

n, p, Q = map(float, stdin.readline().split())
n = int(n)
Q = int(Q)

lst = [[0]*2]*Q

for i in range(Q) :
    lst[i] = list(map(int, stdin.readline().split()))

log_probabilities = [log(comb(n, i)) + i * log(p) + (n - i) * log(1 - p) for i in range(n + 1)]

if (n*p > 1000) & (n*(1-p) > 1000) :
    def times(n, r) :
        p = 1
        for i in range(r+1, n+1) :
            p *= i
        return p

    P_x = [(times(n, i)/times(n-i, 0))*p**i*(1-p)**(n-i) for i in range(n+1)]
    print("\n".join([str(max([sum([P_x[lst[k][0]:lst[k][1]+1][i] >= P_x[lst[k][1]-j] for i in range(lst[k][1]-lst[k][0]+1)])*P_x[lst[k][1]-j] for j in range(lst[k][1]-lst[k][0]+1)])) for k in range(Q)]))

else :
    mu = n*p
    sigma = (n*p*(1-p))**0.5
    for i in range(Q) :
        a, b = lst[i]
        ## case 1 : outer range
        if (a <= mu-sigma) and (b >= mu + sigma) :
            print(0.24197072451914337*2)
            
        ## case 2 : same value
        elif (a <= mu-sigma) and (b == mu) :
            print(0.24197072451914337)
            
        ## case 3 : one value inner range
        elif (a <= mu-sigma) and (b < mu + sigma) :
            solution = (mu + b - ((mu - b)**2 + 4*sigma**2)**0.5)/2
            
            if solution >= 2*mu - b :
                print(norm_pdf(2*mu-b, mu, sigma**2)*2*(b-mu))
            
            elif solution <= a :
                print(norm_pdf(a, mu, sigma**2)*(b-a))
                
            else :
                print(norm_pdf(solution, mu, sigma**2)*(b-solution))
                
        ## case 1~3 for a
        elif (a == mu) and (b >= mu+sigma) :
            print(0.24197072451914337)
            
        elif (a > mu-sigma) and (b >= mu+sigma) :
            solution = ???
        

## optim for all case : mu+sigma, mu-sigma

b = mu+sigma-5
mu
sigma
b-mu

norm_pdf(2*mu-b, mu, sigma**2)*2*(b-mu)
print(0.24197072451914337*2)

## 생각해보니까 이거 안될것같은데, p가 너무 작거나 너무 큰 경우에는 근사가 안됨. 그러면 복잡한 수식을 그대로 돌려야함...