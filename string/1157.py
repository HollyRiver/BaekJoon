aList = {chr(i):0 for i in range(ord('A'),ord('Z')+1)}

txts = "baaa"

for t in txts :
    aList[t.upper()] += 1
    

max_v = 0

for k, v in aList.items() :
    if v > 0 :
        if v > max_v :
            max_v = v
            max_k = k

        elif v == max_v :
            max_k = "?"
            
print(max_k)