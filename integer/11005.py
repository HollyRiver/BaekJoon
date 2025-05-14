N, B = map(int, input().split())

int_dict = {i:chr(i+55) for i in range(10, B+1)}

trans_num = ""

for i in range(32) :
    remain = N%B ## last number
    N = N//B
    
    if remain < 10 :
        trans_num = str(remain) + trans_num
        
    else :
        trans_num = int_dict[remain] + trans_num
        
    if N == 0 :
        break

print(trans_num)