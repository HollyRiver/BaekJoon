## 키와 몸무게 둘 다 큰 사람이 있을 경우 비교가 가능

from sys import stdin

N = int(stdin.readline().rstrip())
status = {i:[0, 0] for i in range(N)}

for i in range(N) :
    w, h = map(int, stdin.readline().split())
    
    status[i] = [w, h]

sorted_dict = sorted(status.items(), key = lambda x : x[1])
sorted_index = [t[0] for t in sorted_dict]
sorted_status = [t[1] for t in sorted_dict]
ranking = [0 for _ in range(N)]

for i in range(N) :
    weight = sorted_status[i][0]
    height = sorted_status[i][1]
    ranking[i] = sum([1 for k in sorted_status[i:] if (k[1] > height) and (k[0] > weight)])+1

first_index = sorted(list(zip(sorted_index, ranking)))

print(" ".join([str(r) for _, r in first_index]))

## 그냥 정렬하지 말고 전역에서 탐색해야 하나... 그럼 시간복잡도가...