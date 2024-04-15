N, r, c = map(int, input().split())

if N == 1 :
    lst = [[0, 1], [2, 3]]
    
else :
    lst = [[0, 1]]

    for i in range(N-1) :
        lst_ = lst[0].copy()
        k = 0
        for j in lst[0]:
            lst_[k] = j+4**(i+1)
            k += 1
        
        lst[0] = lst[0] + lst_

    lst_r = [0, 2]
    
    for i in range(N-1) :
        lst_ = lst_r.copy()
        k = 0
        for j in lst_r:
            lst_[k] = j+2*4**(i+1)
            k += 1
            
        lst_r = lst_r + lst_
    
    for i in lst_r[1:] :
        lst_ = lst[0].copy()
        k = 0
        for j in lst[0] :
            lst_[k] = j+i
            k += 1
        
        lst.append(lst_)

print(lst[r][c])

# 4, 16, 64, 256
# 2, 8, 2, 32, 2, 8, 2, 128

## 0, 16, 64, 256, ... 4^(N-1)
## 0, 32, 128, ... 2*4^(N-1)