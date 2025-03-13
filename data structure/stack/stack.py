## 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램
## push X : 정수 X를 스택에 넣음
## pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력. 스택이 비어있으면 -1
## size : 스택에 들어있는 정수의 개수를 출력
## empty : 스택이 비어있으면 1, 아니면 0 출력
## top : 스택의 가장 위에 있는 정수를 출력. 스택이 비어있으면 -1

from sys import stdin

N = int(stdin.readline().rstrip())
integr_stack = []

for i in range(N) :
    task = stdin.readline().rstrip()
    
    if task[:4] == "push" :
        _, n = task.split()
        integr_stack.append(int(n))
        
    elif task == "pop" :
        if len(integr_stack) == 0 :
            print(-1)
        else :
            print(integr_stack.pop())
    
    elif task == "size" :
        print(len(integr_stack))
        
    elif task == "empty" :
        if len(integr_stack) == 0 :
            print(1)
        else :
            print(0)
    
    elif task == "top" :
        if len(integr_stack) == 0 :
            print(-1)
        else :
            print(integr_stack[-1])