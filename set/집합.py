## 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성

## add x : S에 x를 추가한다. (1 <= x <= 20) S에 x가 이미 있는 경우 무시한다
## remove x : S에서 x를 제거한다. x가 없는 경우 무시
## check x : S에 x가 있으면 1, 없으면 0을 출력
## toggle x : S에 x가 있으면 제거, 없으면 추가
## all : S를 {1, 2, ..., 20}으로 변경
## empty : S를 공집합으로 변경

## 메모리 제한 4MB

S = set()

def set_operation(calcul, x = None) :
    global S
    if calcul == "add" :
        S.add(x)
    elif calcul == "remove" :
        try :
            S.remove(x)
        except :
            return
    elif calcul == "check" :
        print((x in S)*1)
    elif calcul == "toggle" :
        if x in S :
            S.remove(x)
        else :
            S.add(x)
    elif calcul == "all" :
        S = set([i for i in range(1, 21)])
    elif calcul == "empty" :
        S = set()
    

from sys import stdin

for i in range(int(stdin.readline())) :
    inputs = stdin.readline().split()
    
    if len(inputs) == 2 :
        set_operation(inputs[0], int(inputs[1]))
    else :
        set_operation(inputs[0])