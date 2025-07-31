## 인덱스 에러 났는데 고치기 귀찮아... 나중에 하자

from sys import stdin

op_dict = ["-", "+"]

for _ in range(2**16) :
    prefix = stdin.readline().split()
    
    if prefix == "0" :
        break
    
    num_stack = []
    
    for t in prefix[::-1] :
        if t in op_dict :
            new_nums = "("+num_stack[-1]+t+num_stack[-2]+")"
            del num_stack[-1]
            num_stack[-1] = new_nums
            
        else :
            num_stack.append(t)
            
    txt = num_stack[0]
    splited_lst = []
    start = 0
    
    for i, t in enumerate(txt) :
        if t in ["+", "-", "(", ")"] :
            if start != i :
                splited_lst.append(txt[start:i])
                
            splited_lst.append(t)
            start = i+1
            
    usage_len = sum([len(t) for t in splited_lst])
    
    if len(txt) > usage_len :
        splited_lst.append(txt[-(len(txt) - sum([len(t) for t in splited_lst])):])

    op_stack = []
    output = []
    
    for t in splited_lst :
        if t == "(" :
            op_stack.append(t)
            
        elif t == ")" :                    
            for _ in range(len(splited_lst)) :
                if op_stack[-1] == "(" :
                    del op_stack[-1]
                    break
                
                output.append(op_stack.pop())
            
        elif t in op_dict :
            op_stack.append(t)
            
        else :
            output.append(t)

    while len(op_stack) > 0 :
        output.append(op_stack.pop())

    print(" ".join(output))