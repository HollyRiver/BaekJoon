### Ax + B sin(x) = C를 만족하는 해 x를 탐색

from sys import stdin
from math import factorial, log2
import decimal

A, B, C = map(decimal.Decimal, stdin.readline().split())

### 이분 탐색
### f'(x) >= 0이므로 f는 단조증가 함수
### f(x) = Ax + B sin(x) - C : f(0) = -C, f(C/A + 1) > 0 ; B sin(C/A) >= -B >= A
### [0, C/A + 1]를 탐색하면 처리 가능
### 소수점 여섯째 자리까지의 정확도로 처리

### 부동소수점 오차 때문에 테일러급수로 삼각함수 구현해야함
def sin(theta) :
    pi = decimal.Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620")
    x = theta%(2*pi) ## 테일러 급수는 0 근처에서 잘 근사됨
    return sum([(-1)**i*x**(2*i + 1)/factorial(2*i + 1) for i in range(30)])

def f(x) :
    x = decimal.Decimal(str(x))
    return (A*x + B*sin(x) - C)

search_range = [decimal.Decimal('0.0'), C/A + 1]
current_x = sum(search_range)/2
loop_times = int(25*log2(10) + log2(search_range[1])) + 1

for _ in range(loop_times) :
    search_range[(f(current_x) > 0)*1] = current_x ## 0보다 크면 상한, 작으면 하한
    current_x = sum(search_range)/2

print(str(round(current_x, 6))+"0"*(6 - len(str(round(current_x, 6)).split('.')[1])))