## M by N 크기의 보드
## 검은색과 흰색으로 칠해짐
## 해당 보드를 잘라 8 by 8의 체스판으로 만들려고 함
## 8 by 8 크기로 잘라낸 후에, 몇 개의 정사각형을 다시 칠해야 함.
## 다시 칠해야 하는 정사각형의 최소 개수를 출력

from sys import stdin

N, M = map(int, stdin.readline().split())
rows = ["" for _ in range(N)]

for i in range(N) :
    rows[i] = stdin.readline().rstrip()
    
## 방법 1 : 모든 가능한 사각형들을 고려, 다시 칠해야 하는 영역이 가장 작은 한 개의 사각형을 선택
row0 = "BWBWBWBW"
row1 = "WBWBWBWB" ## 0:8

summation_list = []

for i in range(M-7) :
    for j in range(N-7) :
        fst_summation = 0
        snd_summation = 0
        
        for idx, r in enumerate(rows[j:j+8]) :
            current_row = r[i:i+8]
            if idx%2 == 0 :
                fst_summation += sum([1 for k in range(8) if current_row[k] != row0[k]])
                snd_summation += sum([1 for k in range(8) if current_row[k] != row1[k]])
            else :
                snd_summation += sum([1 for k in range(8) if current_row[k] != row0[k]])
                fst_summation += sum([1 for k in range(8) if current_row[k] != row1[k]])
                
        summation_list.append(fst_summation)
        summation_list.append(snd_summation)

print(min(summation_list))