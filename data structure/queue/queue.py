## 정수를 저장하는 큐를 구현
## push X : 정수 x를 큐에 넣음
## pop : 큐에서 가장 앞에 있는 정수를 뺌, 없으면 -1
## size : 큐의 사이즈 출력
## empty : 큐가 비어있으면 1, 아니면 0
## front : 큐의 가장 앞에 있는 정수 출력, 없으면 -1
## back : 큐의 가장 뒤에 있는 정수 출력, 없으면 -1

from collections import deque
from sys import stdin

N = int(stdin.readline().rstrip())
que = deque()

for _ in range(N) :
    task = stdin.readline().rstrip()
    
    if task[:4] == "push" :
        _, n = task.split()
        que.append(int(n))
        
    elif task == "pop" :
        if len(que) == 0 :
            print(-1)
        else :
            print(que.popleft())
            
    elif task == "size" :
        print(len(que))
    
    elif task == "empty" :
        if len(que) == 0 :
            print(1)
        else :
            print(0)
            
    elif task == "front" :
        if len(que) == 0 :
            print(-1)
        else :
            print(que[0])
            
    elif task == "back" :
        if len(que) == 0 :
            print(-1)
        else :
            print(que[-1])