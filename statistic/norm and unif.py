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

## b = [256, 381, 513, 626, 691, 691, 626, 513, 381, 256]
b = [500]*10

if sum([((a[i]-b[i])**2)/5000 for i in range(10)]) < 16.92 :
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