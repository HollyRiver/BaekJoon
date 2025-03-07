## 비밀번호를 랜덤으로 만들어서 기억을 못함
## 메모장에 주소와 비밀번호를 저장
## 메모장에서 비밀번호를 찾는 프로그램

from sys import stdin

N, M = map(int, stdin.readline().split())
pw_dict = {}

for i in range(N) :
     site, pw = stdin.readline().split()
     
     pw_dict[site] = pw

searching = ["" for _ in range(M)]

for j in range(M) :
    searching[j] = stdin.readline().rstrip()
    
for url in searching :
    print(pw_dict[url])