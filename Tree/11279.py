## Max Heap 구현

from sys import stdin

N = int(stdin.readline().rstrip())

class Heap :
    def __init__(self) :
        self.H = []
        
    def __len__(self) :
        return len(self.H)
        
    def heapifyUp(self, k) :
        while (k-1)//2 >= 0 :
            p = (k-1)//2
        
            if self.H[p] < self.H[k] :
                ## swap
                hp = self.H[p]
                self.H[p] = self.H[k]
                self.H[k] = hp
                k = p
            
            else :
                break
        
    def heapifyDown(self) :
        k = 0
        
        while 2*k + 1  <= len(self) - 1 :
            c1 = 2*k + 1
            c2 = 2*k + 2
            
            if c2 >= len(self) or self.H[c1] > self.H[c2] :
                if self.H[c1] > self.H[k] :
                    hk = self.H[k]
                    self.H[k] = self.H[c1]
                    self.H[c1] = hk
                    k = c1
                else :
                    break
            else :
                if self.H[c2] > self.H[k] :
                    hk = self.H[k]
                    self.H[k] = self.H[c2]
                    self.H[c2] = hk
                    k = c2
                else :
                    break
        
    def insert(self, x) :
        if len(self) == 0 :
            self.H.append(x)
        else :
            k = len(self) ## 맨 뒤 인덱스
            self.H.append(x) ## 맨 뒤에 넣음
            self.heapifyUp(k)
        
    def popMax(self) :
        if len(self) == 0 :
            return 0
        else :
            hm = self.H[0]
            self.H[0] = self.H[-1]
            del self.H[-1]
            self.heapifyDown()
            
            return hm
        
H = Heap()

for _ in range(N) :
    n = int(stdin.readline().rstrip())
    
    if n == 0 :
        print(H.popMax())
    else :
        H.insert(n)