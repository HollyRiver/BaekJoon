N = int(input())

output = []

for _ in range(2**32) :
    if N <= 1 :
        break
        
    is_sosu = True
    
    for i in range(2, N//2+1) :
        if N % i == 0 :
            N = N//i
            is_sosu = False
            output.append(str(i))
            break
        
    if is_sosu :
        output.append(str(N))
        break


if len(output) != 0 :
    print("\n".join(output))