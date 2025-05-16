from sys import stdin

T = int(stdin.readline().rstrip())
output = [""]*T

for i in range(T) :
    A, B = map(int, stdin.readline().split())
    
    A_times = A*1
    B_times = B*1
    
    for j in range(2**32) :
        if (A_times == B_times) :
            output[i] = str(A_times)
            break
        elif A_times > B_times :
            if (A_times - B_times)%B == 0 :
                output[i] = str(A_times)
                break
            else :
                B_times += B*((A_times - B_times)//B + 1)
        else :
            if (B_times - A_times)%A == 0 :
                output[i] = str(B_times)
                break
            else :
                A_times += A*((B_times - A_times)//A + 1)
                
print("\n".join(output))