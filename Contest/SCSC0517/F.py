## 쉽다고 생각했는데 어려울 수도 있음...

from sys import stdin

N, M = map(int, stdin.readline().split())

stones = [[0]*M]*N

for i in range(N) :
    stones[i] = [1*(t == "x") for t in stdin.readline().rstrip()]
    
S_dict = [[1, 1, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1]]
C_dict = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1]]
S = 0
C = 0

for i in range(N) :
    for j in range(max([0, M-4])) :
        if stones[i][j:j+5] == [1, 1, 1, 0, 1] :
            a, b, c, d, e = stones[i+1][j:j+5]
            
            if (a == 1 and c == 1 and e == 1) and (stones[i+2][j:j+5] == [1, 1, 1, 1, 1] or stones[i+2][j:j+5] == [1, 0, 1, 1, 1]) :
                stones[i][j:j+5] = [0, 0, 0, 0, 0]
                stones[i+1][j] = 0
                stones[i+1][j+2] = 0
                stones[i+1][j+4] = 0
                stones[i+2][j] = 0
                stones[i+2][j+2] = 0
                stones[i+2][j+3] = 0
                stones[i+2][j+4] = 0
                S += 1
        
        elif stones[i][j:j+5] == [1, 1, 1, 1, 1] :
            a, b, c, d, e = stones[i+1][j:j+5]
            f, g, h, i, j = stones[i+2][j:j+5]
            
            if (a == 1 and e == 1) and (f == 1 and j == 1) :
                stones[i][j:j+5] = [0, 0, 0, 0, 0]
                stones[]
            
            
    
## 그냥 10*10이니까 무지성 브루트 포싱 한다음, 문제가 생기면 기점으로 돌아가서 다시?

## 무지성 하드코딩 대입
## 생각보다 모양이 한정적임
## [-, -, 1, 1, 1, 1, 1]
## [-, 1, 1, 1, 1, 1, 1]
## [1, 1, 1, 1, 1, 1, 1]
## [1, 1, 1, 1, 1, 1, -]
## [1, 1, 1, 1, 1, -, -]

## [1, 1, 1, -, -]
## [1, 1, 1, 1, -]
## [1, 1, 1, 1, 1]
## [1, 1, 1, 1, 1]
## [1, 1, 1, 1, 1]
## [-, 1, 1, 1, 1]
## [-, -, 1, 1, 1]