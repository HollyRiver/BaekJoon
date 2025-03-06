## 뭔 서사가;;

## 포켓몬의 이름을 보면 번호를 말하거나, 번호를 보면 이름을 말하기 -> 딕셔너리 최고

# from sys import stdin

# N, M = map(int, stdin.readline().split())
# poke_pedia = {}

# for i in range(N) :
#     poke_pedia[stdin.readline()] = i
    
# for i in range(M) :
#     input_value = stdin.readline()
    
#     try :
#         int(input_value)
#         print(list(poke_pedia.keys())[int(input_value)-1])
    
#     except :
#         print(poke_pedia[input_value]+1)

##----------트라이 문법이 느린가?----------
# from sys import stdin

# N, M = map(int, stdin.readline().split())

# poke_name = ["" for _ in range(N)]

# for i in range(N) :
#     poke_name[i] = stdin.readline()
    
# for _ in range(M) :
#     input_value = stdin.readline()

from sys import stdin

N, M = map(int, stdin.readline().split())
poke_pedia = {}

for i in range(N) :
    poke_pedia[stdin.readline().rstrip()] = i
    
index_pedia = {v:k for k, v in poke_pedia.items()}
    
for i in range(M) :
    input_value = stdin.readline().rstrip()
    
    if (input_value[0].isupper()) or (input_value[-1].isupper()) :
        print(poke_pedia[input_value]+1)
    else :
        print(index_pedia[int(input_value)-1])
        
## 결론 -> 탐색에서는 딕셔너리가 제일 빠르다.