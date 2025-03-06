# 1, n

# 1, m

# O, X

# 가고싶어하는 학생 수가 많은 순서대로 여행 후보지 번호를 출력
# 가고 싶어하는 학생 수가 같다면, 번호가 작은 순서대로 출력


# 입력
n, m = map(int, input().split())
summation = [0 for _ in range(m)]

for _ in range(n) :
    tmpt = list(map(int, input().split()))
    
    for i, t in enumerate(tmpt) :
        summation[i] += t

sorted_sum = sorted(summation, reverse = True)
ranking = [-1 for _ in range(m)]

for rank, r in enumerate(sorted_sum) :
    for i, s in enumerate(summation) :
        if (ranking[i] == -1) & (r == s) :
            ranking[i] = rank
            break
        
order = [[idx for idx, j in enumerate(ranking) if j == i][0] + 1 for i in range(m)]

print(" ".join([str(r) for r in order]))