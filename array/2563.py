from sys import stdin

N = int(stdin.readline().rstrip())

paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N) :
    side, bottom = map(int, stdin.readline().split())
    
    for i in range(bottom-10, bottom) :
        paper[i][side:side+10] = [1]*10
        
print(sum([sum(r) for r in paper]))