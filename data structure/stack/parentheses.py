## 괄호 문자열 PS는 두 개의 괄호 기호인 '(', ')'만으로 구성되어 있는 문자열임
## 괄호의 모양이 바르게 구성된 문자열을 괄호 문자열이라고 부름 Valid PS : VPS
## 한 쌍의 괄호 기호로 된 "()" 문자열은 기본 VPS라고 함
## x가 VPS라면, 이것을 하나의 괄호에 넣은 새로운 문자열 "(x)"도 VPS가 됨
## 두 VPS x와 y를 concatenation시킨 새로운 문자열 xy도 VPS가 됨
## 입력으로 주어진 괄호 문자열이 VPS인지 아닌지를 판단해서 그 결과를 YES와 NO로

from sys import stdin

T = int(stdin.readline().rstrip())
txts = ["" for _ in range(T)]

for i in range(T) :
    txts[i] = stdin.readline().rstrip()
    
for txt in txts :   
    txt_stack = [""]
    is_VPS = True
    
    for t in txt :
        if t == "(" :
            txt_stack.append(t)
        else :
            if txt_stack[-1] == "(" :
                del txt_stack[-1]
            else :
                is_VPS = False
                break
            
    if (len(txt_stack) == 1) and (is_VPS) :
        print("YES")
        
    else :
        print("NO")