from sys import stdin

for _ in range(2**32) :
    n = int(stdin.readline().rstrip())
    
    if n == -1 :
        break
    
    fac = [1]

    for i in range(2, n//2 + 1) :
        if n % i == 0 :
            fac.append(i)
    
    if sum(fac) == n :
        print(f"{n} = {" + ".join([str(f) for f in fac])}")
        
    else :
        print(f"{n} is NOT perfect.")