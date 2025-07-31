from sys import stdin
from decimal import Decimal, getcontext

getcontext().prec = 300 ## 누가 이기나 봅세

T = int(stdin.readline().rstrip())

# 이분법으로 풀 수 없는 문제인가 보오
# for _ in range(T) :
#     n = Decimal(stdin.readline().rstrip())
#     approx_root = n**(Decimal("1.0")/Decimal("3.0"))
#     half_width = Decimal("1e-5")
#     squares = Decimal("3")
    
#     search_range = [approx_root - half_width, approx_root + half_width]
#     current_x = approx_root
#     loop_times = 2000 ## 1e-5 -> 1e-305
    
#     for _ in range(loop_times) :
#         search_range[(current_x**squares >= n)*1] = current_x
#         current_x = sum(search_range)/Decimal("2")
        
#     print(str(current_x).split(".")[0] + "." + str(current_x).split(".")[1][:10])

## 3차 방정식의 해를 이용하거나, 뉴턴 랩슨 방법을 사용하거나, 수치적으로 접근해야 할 것 같음
## 뉴턴 랩슨 방법 하니까 바로 됨;; 근데 정확도를 어디까지 할건지를 설정해줘야 하는데 어케함
def f(x, N) :
    return (x**Decimal('3') - N)

def f_prime(x) :
    return Decimal("3")*x**Decimal("2")

for _ in range(T) :
    N = Decimal(stdin.readline().rstrip())
    x = N**(Decimal("1.0")/Decimal("3.0"))
    
    for _ in range(100) :
        x = x - f(x, N)/f_prime(x)
        
    print(str(x).split(".")[0] + "." + str(x).split(".")[1][:10])
