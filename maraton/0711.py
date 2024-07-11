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