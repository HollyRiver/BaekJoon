## 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램
## 입력의 종료조건으로 맨 마지막에 온점 하나가 들어온다.

# from sys import stdin
# txts = []

# for _ in range(2**10) :
#     txt = stdin.readline().rstrip()
    
#     if txt == "." :
#         break
    
#     txts.append(txt)

# balance_break = False

# for txt in txts :
#     parenth_start = {"{":0, "[":0, "(":0}
#     parenth_end = {")" : "(", "}" : "{", "]" : "["}
    
#     for t in txt :
#         if t in parenth_start.keys() :
#             parenth_start[t] += 1
#         elif t in parenth_end.keys() :
#             if parenth_start[parenth_end[t]] > 0 :
#                 parenth_start[parenth_end[t]] -= 1
#             else :
#                 balance_break = True
#                 break

#     if (not balance_break) and ((parenth_start["{"] == 0) and (parenth_start["("] == 0) and (parenth_start["["] == 0)) :
#         print("yes")
#     else :
#         print("no")

#     balance_break = False
    

## 이렇게 풀면 안됨 ㅇㅇ

from sys import stdin
txts = []

for _ in range(2**16) :
    txt = stdin.readline().rstrip()
    
    if txt == "." :
        break
    
    txts.append(txt)
    
balance_break = False

for txt in txts :
    parenth_start = ["[", "("]
    parenth_end = {")" : "(", "]" : "["}
    
    text_stack = [""]
    
    for t in txt :
        if t in parenth_start :
            text_stack.append(t)
        elif t in parenth_end.keys() :
            if parenth_end[t] == text_stack[-1] :
                del text_stack[-1]
            else :
                balance_break = True
                break

    if (not balance_break) and (len(text_stack) == 1) :
        print("yes")
    else :
        print("no")

    balance_break = False