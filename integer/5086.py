from sys import stdin

for _ in range(2**32) :
    A, B = map(int, stdin.readline().rstrip().split())
    
    if A == 0 and B == 0 :
        break
    
    if A % B == 0 :
        print("multiple")
        
    elif B % A == 0 :
        print("factor")
        
    else :
        print("neither")