from sys import stdin

N = int(stdin.readline().rstrip())

Cs = [0]*N

for i in range(N) :
    Cs[i] = int(stdin.readline().rstrip())
    

outputs = [""]*N

for i, C in enumerate(Cs) :
    get_C = C
    output = [0]*4
    
    for j, t in enumerate([25, 10, 5, 1]) :
        output[j] = get_C//t
        get_C = get_C%t
        
    outputs[i] = " ".join([str(o) for o in output])
    

print("\n".join(outputs))