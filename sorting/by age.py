## 회원들을 나이가 증가하는 순으로
## 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

from sys import stdin

N = int(stdin.readline().rstrip())
member_dict = {}

for _ in range(N) :
    age, name = stdin.readline().split()
    age = int(age)
    
    if age in member_dict.keys() :
        member_dict[age] = member_dict[age] + [name]
    
    else :
        member_dict[age] = [name]

sorted_age = sorted(member_dict.keys())

for k in sorted_age :
    for n in member_dict[k] :
        print(str(k) + " " + n)