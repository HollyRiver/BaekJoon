from sys import stdin

N = int(stdin.readline().rstrip())
output = [""]*N

for i in range(N) :
    n = int(stdin.readline().rstrip())

    if n <= 2 :
        output[i] = "2"
    else :
        for j in range(2**8) :
            is_prime = True
            
            for k in range(2, (n**0.5)//1 + 1) :
                if current//k == 0 :
                    is_prime = False
                    break

            if is_prime :
                output[i] = str(n)
                break

            n += 1

print("\n".join(output))