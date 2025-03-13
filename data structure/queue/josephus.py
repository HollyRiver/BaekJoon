## 요세푸스 문제
## 1번부터 N번까지 원을 이루면서 앉아있고, 양의 정수 k <= N이 주어짐.
## 순서대로 K번째 사람을 제거.
## 한 사람이 제거되면 남은 사람들로 이뤄진 원을 따라 해당 과정을 반복
## N명의 사람이 모두 제거될 때까지 반복
## 제거된 위치부터 다시 세어나가는 방식인듯

N, K = map(int, input().split())

permut = [i for i in range(N)]
josep = []

removal_index = 0

for i in range(N) :
    removal_index = (removal_index + K - 1)%len(permut)
    josep.append(permut.pop(removal_index)+1)
    
print("<" + ", ".join([str(n) for n in josep]) + ">")
    
    
## i를 리스트의 길이로 나눈 나머지에 해당하는 인덱스를 빼면...