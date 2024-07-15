N, M = map(int, input().split())

Nova = sorted(list(map(int, input().split())))
Origin = sorted(list(map(int, input().split())))

bind = 0
time = 0
Origin_bind = 0
Origin_time = 0

for i in range(len(Nova)) :
    if i == 0 :
        bind += 1 
        
    else :
        time += Nova[i] - Nova[i-1]
        
    if time >= 100 :
        bind += 1
        time = 0
        
for j in range(len(Origin)) :
    if j == 0 :
        Origin_bind += 1
        
    else :
        Origin_time += Origin[j] - Origin[j-1]
        
    if Origin_time >= 360 :
        Origin_bind += 1
        Origin_time = 0
        
print(str(bind) + " " + str(Origin_bind))

##------------------------

from sys import stdin
import copy

N, M, K = map(int, input().split())

D = [0]*N
P = [0]*K
Q = [0]*K
HP = [0]
MESO = [0]

for i in range(N) :
    D[i] = int(stdin.readline().strip())

D.sort(reverse = True)

for j in range(K) :
    P[j], Q[j] = map(int, stdin.readline().strip().split())

def all_case(K, t = 0, lstP = [], lstQ = [], index = 0) :
    for k in range(t, K) :
        HP.append(lstP+[P[k]])
        MESO.append(lstQ+[Q[k]])
        
        if k+1 < K :
            all_case(K, t = k+1, lstP = HP[index-1], lstQ = MESO[index-1], index = index)

all_case(K)

HP[0] = [0]
MESO[0] = [0]

output = 0

for k in range(M) :
    temp = copy.deepcopy(HP)
    for i in range(2**K) :
        for j in range(len(HP[i])) :
            remain = temp[i][j]%D[k]
            if remain != 0 :
                temp[i][j] = temp[i][j] + D[k] - remain
                
    output += max([sum(MESO[i]) for i in range(2**K) if sum(temp[i]) <= D[k]*900])

print(output)


##-------------------

N = int(input())

lst = list(map(int, input().split()))

print(len([i for i in lst if i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]]))

##------------------------

N = input()
output = 0
creator = 0

if len(N) < 2 :
    start = 0
else :
    start = 9*10**(len(N)-2)

for i in range(start, int(N)) :
    creator = i + sum([int(j) for j in list(str(i))])
    print(creator)
    
    if creator == int(N) :
        output = i
        break

print(output)

##-------------------------

N = int(input())

lst = [[1, 1]]

for i in range(20000) :
    lst.append([lst[i][1]+1, lst[i][1]+(i+1)*6])

print([i+1 for i in range(len(lst)) if lst[i][0] <= N <= lst[i][1]][0])


##-----------------------

lst = [1,2,3,4,5]
K = len(lst)

summation = [[0,0,0]]*int(K*(K-1)*(K-2)/(3*2))

def combination(lst, start = 0, ind = 0) :
    for i in range(start, K-2) :
        summation[i][ind] += lst[i]
        temp = lst[i+1:]
        
        combination(temp, i+1, ind+1)
        