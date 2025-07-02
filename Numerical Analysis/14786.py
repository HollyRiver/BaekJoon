from sys import stdin
from math import sin, log2

A, B, C = map(int, stdin.readline().split())

def f(x) :
    return (A*x + B*sin(x) - C)

search_range = [0.0, C/A + 1]
current_x = sum(search_range)/2

loop_times = int(log2(search_range[1]) + 10*log2(10)) + 1

for _ in range(loop_times) :
    search_range[(f(current_x) > 0)*1] = current_x ## 0보다 크면 상한, 작으면 하한
    current_x = sum(search_range)/2

# while 쓰기 싫음 ㅇㅇ
while (search_range[1] - search_range[0]) >= 1e-10 :
    search_range[(f(current_x) > 0)*1] = current_x ## 0보다 크면 상한, 작으면 하한
    current_x = sum(search_range)/2
    
print(current_x)