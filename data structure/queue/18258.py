from sys import stdin

N = int(stdin.readline().rstrip())
Q = []
start = 0

for _ in range(N) :
    R = stdin.readline().rstrip()
    
    if R[:4] == "push" :
        Q.append(int(R.split()[-1]))
    elif R == "pop" :
        if len(Q) > start :
            print(Q[start])
            start += 1
        else :
            print(-1)
    elif R == "size" :
        print(len(Q) - start)
    elif R == "empty" :
        print((len(Q) == start)*1)
    elif R == "front" :
        if len(Q) > start :
            print(Q[start])
        else :
            print(-1)
    else :
        if len(Q) > start :
            print(Q[-1])
        else :
            print(-1)