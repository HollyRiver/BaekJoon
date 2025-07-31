from sys import stdin

N = int(stdin.readline().rstrip())
nums = list(map(int, stdin.readline().split()))
S = []

current_num = 1
i = 0

while current_num < N+1 :
    if len(S) > 0 and S[-1] == current_num :
        del S[-1]
        current_num += 1
    else :    
        if i < N :
            if nums[i] != current_num :
                S.append(nums[i])
            else :
                current_num += 1
                
            i += 1
            
        else :
            if S[-1] != current_num :
                break

    
if len(S) == 0 :
    print("Nice")
else :
    print("Sad")