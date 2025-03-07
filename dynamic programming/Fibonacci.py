## N번째 피보나치 수를 구하는 함수

def fibonacci(n) :
    if n == 0 :
        print(0)
        return 0
    elif n == 1 :
        print(1)
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
## fibonacci(3)을 호출하면...
## fibonacci(2)와 fibonacci(1)을 호출
## fibonacci(2)는 fibonacci(1)과 fibonacci(0)를 호출
## fibonacci(1)은 1을 출력하고 1을 리턴
## fibonacci(0)는 0을 출력하고 0을 리턴
## fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고 1을 리턴
## 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴
## fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴

## 1은 2번 출력되고, 0은 한번 출력
## fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되나?

from sys import stdin

T = int(stdin.readline().rstrip())
cases = [0 for _ in range(T)]

for t in range(T) :
    cases[t] = int(stdin.readline().rstrip())
    
## 3 -> 2/1 -> 1, 0, 1
## 2 -> 1/0 -> 1, 0
## 하위 2개를 합산한 만큼 출력함

## 1은 0, 1
## 2는 1, 1
## 3은 1, 2
## 4는 2, 3
## 5는 3, 5 ...

## 초반은 그냥 하드코딩 때려버리고, 4부터 점화식으로 계산하자.

zero_case = [1, 0, 1, 1]
one_case = [0, 1, 1, 2]

for i in range(37) :
    zero_case.append(sum(zero_case[-2:]))
    one_case.append(sum(one_case[-2:]))
    
for c in cases :
    print(str(zero_case[c]) + " " + str(one_case[c]))