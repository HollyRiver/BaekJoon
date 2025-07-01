from sys import stdin

N = int(stdin.readline().rstrip())
S = list(stdin.readline().rstrip())

## O가 두 번 이상 반복되면 안됨
## H가 2/3이 아니면 안됨

## HHHHHOH -> HOH 제거
## 앞에 나온 H 2개보다 O가 더 많은 경우 -> 안자름
## 앞에서 나온 H 두묶음 개수보다 O가 많으면 안됨

if N%3 == 0 :
    if sum([1 for s in S if s == "O"]) == N//3 :
        if S[0] == "O" :
            print("mix")
            
        else :
            h = 0
            o = 0
            i = 0
            
            for _ in range(N) :
                if len(S) <= i :
                    break
                
                if S[i] == "H" :
                    h += 1
                    i += 1
                else :
                    if S[i+1] == "H" :
                        o += 1
                        
                        if h*2 >= o :
                            del S[i-1:i+2]
                            i -= 1 + (S[i-2] == "O")*1
                            h -= 1
                            o -= 1
                        
                        else :
                            i += 1
                    else :
                        print("mix")
                        break
                    
            if len(S) == 0 :
                print("pure")
            
            else :
                h = 0
                o = 0
                i = 0
                
                for _ in range(N) :
                    if len(S) <= i :
                        break
                    
                    if S[i] == "H" :
                        h += 1
                        i += 1
                    else :
                        if S[i+1] == "H" :
                            o += 1
                            
                            if h*2 >= o :
                                del S[i-1:i+2]
                                i -= 1 + (S[i-2] == "O")*1
                                h -= 1
                                o -= 1
                            
                            else :
                                i += 1
                        else :
                            print("mix")
                            break
                        
            if len(S) == 0 :
                print("pure")
            
    else :
        print("mix")
else :
    print("mix")
    
    
## 실패!