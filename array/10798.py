from sys import stdin

txts = [""]*5

for i in range(5) :
    txts[i] = stdin.readline().rstrip()
    

output = ""


for j in range(15) :
    for i in range(5) :
        output += txts[i][j:j+1]
        
print(output)