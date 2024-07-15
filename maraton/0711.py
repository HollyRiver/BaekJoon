lst = list(map(int, input().split()))

max_score = [100*round((i+1.1)/2) for i in range(9)]

hacker = False

if sum(lst) < 100 :
    print("none")

else :
    for i in range(9) :
        if lst[i] > max_score[i] :
            print("hacker")
            hacker = True
            break
            
    if not hacker :
        print("draw")
        
##--------------------------------

N = int(input())
lst = list(map(int, input().split()))
cluster = int(input())

storage = 0

for l in lst :
    if l%cluster == 0 :
        storage += l//cluster*cluster
        
    else :
        storage += (l//cluster + 1)*cluster
        
print(storage)

##---------------------------------

lst = [int(i) for i in list(str(input()))]

ten_num = 0

for i in range(len(lst)) :
    if lst[i] == 1 :
        ten_num += 2**(len(lst)-1-i)
    

if len(lst)%3 == 0 :
    eight_len = len(lst)//3
else :
    eight_len = len(lst)//3 + 1

output_lst = [0]*eight_len

for i in range(eight_len) :
    output_lst[i] = int(ten_num//8**(eight_len-1-i))
    ten_num -= 8**(eight_len-1-i)*output_lst[i]
    
"".join([str(i) for i in output_lst])


lst = [int(i) for i in list(str(input()))]

if len(lst)%3 == 0 :
    eight_len = len(lst)//3
else :
    eight_len = len(lst)//3 + 1
    
output_lst = [0]*eight_len

for i in range(len(lst)) :
    output_lst[-(i//3+1)] = output_lst[-(i//3+1)] + lst[-(i+1)]*2**(i%3)

"".join([str(i) for i in output_lst])

##----------------------------------

N, M = map(int, input().split())

card_list = list(map(int, input().split()))

all_case = []

def combination(sub_list = [], start = 0) :
    for i in range(start, len(card_list)) :
        print(sub_list)
        sub_list = sub_list + [card_list[i]]
        print(sub_list, card_list[i])
        
        if len(sub_list) < 3 :
            if (len(sub_list) == 2) and (i == len(card_list)-1) :
                sub_list = []
                
            else :
                combination(sub_list, i+1)
            
        elif len(sub_list) == 3 :
            all_case.append(sub_list)
            ## 해당 조건문에 들어오기는 하지만, sub_list가 변경되진 않음
            if sub_list[2] == card_list[-1] :
                if sub_list[1] == card_list[-2] :
                    sub_list = []
                else :
                    sub_list = [sub_list[0]]
            else :
                sub_list = sub_list[:2]

combination()

all_case



N, M = map(int, input().split())

card_list = list(map(int, input().split()))

all_case = []

def combination(sub_list = [], start = 0) :
    if len(sub_list) == 3 :
        all_case.append(sub_list)
        return
    
    for i in range(start, len(card_list)) :
        combination(sub_list + [card_list[i]], i + 1)

combination()

for case in all_case:
    print(case)
    
    
##--------------------------

L = int(input())

txt = input()

str_dict = {chr(x): i for x, i in zip(range(97, 123), range(1, 27))}

hashing = 0

for i in range(L) :
    hashing += str_dict[txt[i]]*31**i
    
print(hashing)