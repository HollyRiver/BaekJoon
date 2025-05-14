N, B = input().split()

B = int(B)


int_dict = {chr(i+55):i for i in range(10, B+1)}

s = 0

for i, n in enumerate(N[::-1]) :
    if n in int_dict.keys() :
        s += int_dict[n]*B**i
        
    else :
        s += int(n)*B**i

print(s)