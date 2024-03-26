N, M = map(int, input().split())

lsts = []

for i in range(N) :
    lsts.append(0)

for i in range(M) :
    first, last, number = map(int, input().split())
    for j in range(first-1, last) :
        lsts[j] = number

output = ""
    
for v in lsts :
    output = output + " " + str(v)

print(output[1:])