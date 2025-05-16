## 두 양의 정수 a > b에 대하여 a = bq + r, (0 <= r < b)라 하면
## a, b의 최대공약수는 b, r의 최대공약수와 같다.
## a, b의 곱에 최대공약수를 나눈 값은 최소공배수이다.
from sys import stdin

T = int(stdin.readline().rstrip())
output = [""]*T

for i in range(T) :
    A, B = list(map(int, stdin.readline().split()))
    ints = [A, B]
    
    ints.sort(reverse = True)
    
    for j in range(2**16) :
        R = ints[0]%ints[1]
        
        if R == 0 :
            output[i] = str((A*B)//ints[1])
            break
        else :
            ints = [ints[1], R]
    

print("\n".join(output))