N, A, B = map(int, input().split())

Due = list(map(int, input().split()))
term = [0]*(N-1)

for i in range(N-1) :
    term[i] = Due[i+1] - Due[i]
    
X = max(term)//B