from sys import stdin

## 원형 양방향 연결 리스트...인데 그냥 리스트로 풀수도 있긴 함

N = int(stdin.readline().rstrip())
nums = list(map(int, stdin.readline().split()))

class Node :
    def __init__(self, key = None) :
        self.key = key
        self.next = None
        self.prev = None
        
class DLL :
    def __init__(self) :
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.length = 0
        
    def __len__(self) :
        return self.length
        
    def PushFront(self, key) :
        if len(self) == 0 :
            self.dummy.next = self.dummy.prev = Node(key)
            self.dummy.next.next = self.dummy.next.prev = self.dummy
            self.length += 1
        else :
            new_node = Node(key)
            new_node.next = self.dummy.next
            self.dummy.next.prev = new_node
            self.dummy.next = new_node
            new_node.prev = self.dummy
            self.length += 1
            
    def delete(self, x) :
        if len(self) == 0 :
            return None, None
        else :
            k = x.key
            xn = x.next
            x.next.prev = x.prev
            x.prev.next = x.next
            del x
            self.length -= 1
            
            return k, xn
            
## 리스트로 하면 O(n^2)
## 양방향 연결 리스트로 하면 O(n)인가
## 팩트는 O(n^2)으로 해도 시간은 충분하다는거임
    
Nums = DLL()
        
for n in nums[::-1] :
    Nums.PushFront(n)
    
times, xn = Nums.delete(Nums.dummy.next)
idxs = ["1"]

for _ in range(N-1) :
    if times > 0 :
        for _ in range(times-1) :
            xn = xn.next
            
            if xn.key == None :
                xn = xn.next
    else :
        for _ in range(abs(times)) :
            xn = xn.prev
            
            if xn.key == None :
                xn = xn.prev
                
    if xn.key == None :
        xn = xn.next

    times, xn = Nums.delete(xn)
    idxs.append(str(nums.index(times)+1))

print(" ".join(idxs))


## 그냥 리스트로 풀랜다
from sys import stdin

N = int(stdin.readline().rstrip())
Origin_nums = list(map(int, stdin.readline().split()))
nums = Origin_nums.copy()
idxs = ["1"]
times = nums.pop(0)
current_idx = 0
total_times = times

for _ in range(N-1) :
    n = len(nums)
    
    if times > 0 :
        current_idx = (current_idx + times - 1)%n
    else :
        current_idx = (current_idx + times)%n
        
    times = nums.pop(current_idx)
    total_times += times
    if total_times == N :
        idxs.append(str(N))
    else :
        idxs.append(str(total_times%N))

print(" ".join(idxs))


## 다시 원형 양방향 리스트로 가자...

from sys import stdin

N = int(stdin.readline().rstrip())
Nums = list(map(int, stdin.readline().split()))

class Node :
    def __init__(self, key = None, value = None) :
        self.key = key
        self.value = value
        self.next = self
        self.prev = self
        
class DLL :
    def __init__(self) :
        self.head = Node()
        self.length = 0
    
    def __len__(self) :
        return self.length
    
    def PushFront(self, node) :
        if self.length == 0 :
            self.head.next = node
            self.head.prev = node
            node.next = self.head
            node.prev = self.head
            self.length += 1
        else :
            self.head.next.prev = node
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
            self.length += 1
            
    def pop(self, node) :
        if self.length == 0 :
            return None
        else :
            np = node.prev
            nn = node.next
            np.next = nn
            nn.prev = np
            k = node.key
            del node
            self.length -= 1
            
            if nn.key == None :
                return k, nn.next
            else :
                return k, nn
        
dll = DLL()

for i in range(N-1, -1, -1) :
    dll.PushFront(Node(i+1, Nums[i]))
    
current_node = dll.head.next
v = current_node.value
idxs = []

k, current_node = dll.pop(current_node)
idxs.append(str(k))

for _ in range(N-1) :
    if v > 0 :
        for _ in range(v-1) :
            if current_node.next.key == None :
                current_node = current_node.next.next ## pass dummy
            else :
                current_node = current_node.next
        if current_node.key == None :
            current_node = current_node.next
    else :
        for _ in range(abs(v)) :
            if current_node.prev.key == None :
                current_node = current_node.prev.prev
            else :
                current_node = current_node.prev
                
    v = current_node.value
    k, current_node = dll.pop(current_node)
    idxs.append(str(k))
    
print(" ".join(idxs))