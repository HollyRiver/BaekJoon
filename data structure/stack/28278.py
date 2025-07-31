from sys import stdin

N = int(stdin.readline().rstrip())
    
S = []

for _ in range(N) :
    R = stdin.readline().rstrip()
    if len(R) > 1 :
        x = int(R.split()[-1])
        S.append(x)
    elif R == "2" :
        if len(S) > 0 :
            print(S.pop())
        else :
            print(-1)
    elif R == "3" :
        print(len(S))
    elif R == "4" :
        if len(S) > 0 :
            print(0)
        else :
            print(1)
    else :
        if len(S) > 0 :
            print(S[-1])
        else :
            print(-1)