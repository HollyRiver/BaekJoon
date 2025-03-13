## 설탕을 정확히 N 킬로그램 배달
## 3kg/5kg만 있음
## 정확하게 N kg 배달해야 할 때, 몇 개의 봉지를 가져가야 하나?

N = int(input())

## 어차피 N이 최대 5000이니까, 무작정 5로 최대한 나눠놓고 나머지를 3으로 떨어지게 만들면 될듯.
## 안되면 -1 출력

printing = False

for i in range(1000) :
    current = N%5 + 5*i

    if current > N :
        break

    if current%3 == 0 :
        print(N//5 - i + current//3)
        printing = True
        break

if not printing :
    print(-1)