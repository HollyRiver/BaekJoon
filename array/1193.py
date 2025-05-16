X = int(input())

for i in range(1, 5000) :
    if X > i :
        X -= i
        
    else :
        if i % 2 == 0 :
            output = f"{X}/{i+1-X}"
            break
        
        else :
            output = f"{i+1-X}/{X}"
            break
        
print(output)