from sys import stdin

aray = [0]*9

for i in range(9) :
    aray[i] = list(map(int, stdin.readline().split()))

max_v = 0
idx_row = 1
idx_col = 1
    
for i in range(9) :
    for j in range(9) :
        v = aray[i][j]
        
        if v > max_v :
            max_v = v
            idx_row = i
            idx_col = j
            
print(max_v)
print(f"{idx_row+1} {idx_col+1}")