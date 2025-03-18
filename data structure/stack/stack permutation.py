## 후입선출 자료구조
## 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘여놓아서 하나의 수열을 만들 수 있음
## 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다
## 임의의 수열이 주어졌을 때, 스택을 이용해 그 수열을 만들 수 있는지, 없는지.
## 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지 알아내자.

from sys import stdin

n = int(stdin.readline().rstrip())
permut_list = [0 for _ in range(n)]

for i in range(n) :
    permut_list[i] = int(stdin.readline().rstrip())
    
stacking = []

## 넣은 시점에서 이미 넣은 것을 다음 수로 빼내려고 하면 연산이 불가능함
## 다음 숫자가 더 크거나 1을 뺀 수여야만 뺄 수 있음. 그냥 이건 빼면서 처리하면 됨.

current_num = 1
output = []

for p in permut_list :
    ## p - 1만큼 append
    if current_num <= p :
        for i in range(current_num, p) :
            stacking.append(i)
            output.append("+")
        output.append("+")
        output.append("-")
        
        current_num = p+1
    
    else :
        if p == stacking[-1] :
            del stacking[-1]
            output.append("-")
        
        else :
            print("NO")
            output = None
            break

if output != None :
    print("\n".join(output))