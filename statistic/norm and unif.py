## No.26523
## 2 sigma over : under 5 % / n의 30% 이상이 0.언더, 0.9오버면 유니폼으로 간주해보자.

from sys import stdin

lst = [0]*5000
a = [0]*20

for i in range(5000) : 
    lst[i] = float(stdin.readline())

for i in lst :
    if (i <= 0.05) :
        a[0] += 1
    elif (i <= 0.1) :
        a[1] += 1
    elif (i <= 0.15) :
        a[2] += 1
    elif (i <= 0.2) :
        a[3] += 1
    elif (i <= 0.25) :
        a[4] += 1
    elif (i <= 0.3) :
        a[5] += 1
    elif (i <= 0.35) :
        a[6] += 1
    elif (i <= 0.4) :
        a[7] += 1
    elif (i <= 0.45) :
        a[8] += 1
    elif (i <= 0.5) :
        a[9] += 1
    elif (i <= 0.55) :
        a[10] += 1
    elif (i <= 0.6) :
        a[11] += 1
    elif (i <= 0.65) :
        a[12] += 1
    elif (i <= 0.7) :
        a[13] += 1
    elif (i <= 0.75) :
        a[14] += 1
    elif (i <= 0.8) :
        a[15] += 1
    elif (i <= 0.85) :
        a[16] += 1
    elif (i <= 0.9) :
        a[17] += 1
    elif (i <= 0.95) :
        a[18] += 1
    else :
        a[19] += 1

b = [250]*20
sum([((a[i]-b[i])**2)/250 for i in range(20)])

if sum([((a[i]-b[i])**2)/250 for i in range(20)]) < 30.14 :
    print("A")
else :
    print("B")
    
    
from sys import stdin

lst = [0]*5000

for i in range(5000) : 
    lst[i] = float(stdin.readline())


if (0.24 < lst[1250] < 0.26) :
    print("A")
else :
    print("B")
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sr = pd.Series(lst)
sr.to_csv("lst.csv")
    
# 0.8862
# 0.1577 -> 0.1779 -> 889.5
# 0.2854 -> 0.3221 -> 1610.5




## No.26523
## 2 sigma over : under 5 % / n의 30% 이상이 0.언더, 0.9오버면 유니폼으로 간주해보자.

from sys import stdin

lst = [0]*5000
a = [0]*10

for i in range(5000) : 
    lst[i] = float(stdin.readline())

for i in lst :
    if (i <= 0.1) :
        a[0] += 1
    elif (i <= 0.2) :
        a[1] += 1
    elif (i <= 0.3) :
        a[2] += 1
    elif (i <= 0.4) :
        a[3] += 1
    elif (i <= 0.5) :
        a[4] += 1
    elif (i <= 0.6) :
        a[5] += 1
    elif (i <= 0.7) :
        a[6] += 1
    elif (i <= 0.8) :
        a[7] += 1
    elif (i <= 0.9) :
        a[8] += 1
    else :
        a[9] += 1


## 더 정확한 통계량을 사용해야 될 것 같음, 아니면 접근 자체를 다르게 해야 하던가.

b = [256, 381, 513, 626, 691, 691, 626, 513, 381, 256]

if sum([((a[i]-b[i])**2)/556.9 for i in range(10)]) > 16.92 :
    print("A")
else :
    print("B")
    
    
import random
import math
import pandas as pd
lst2 = [random.normalvariate(0.5, math.sqrt(0.1)) for i in range(5000)]
sr2 = pd.Series(lst2)
sr2.to_csv("lst2.csv", index=False)


from sys import stdin

a = ""
for i in range(100) :
    k = 0
    for j in range(5000) :
        if float(stdin.readline()) < 0.05 :
            k += 1
    if k > 180 :
        a = a+"A"
    else : 
        a = a+"B"
    
    if i != 99 :
        a = a+"\n"
        
print(a)