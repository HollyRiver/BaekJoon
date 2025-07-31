from sys import stdin

N = int(stdin.readline().rstrip())

class Node :
    def __init__(self, key = None) :
        self.key = key
        self.left = None
        self.right = None

class Deque :
    def __init__(self) :
        self.head = None
        self.tail = None
        self.length = 0
        
    def __len__(self) :
        return self.length
    
    def PushFront(self, x) :
        if self.head == None :
            self.head = self.tail = Node(x)
        else :
            self.head.left = Node(x)
            self.head.left.right = self.head
            self.head = self.head.left
            
        self.length += 1
    
    def PushBack(self, x) :
        if self.tail == None :
            self.head = self.tail = Node(x)
        else :
            self.tail.right = Node(x)
            self.tail.right.left = self.tail
            self.tail = self.tail.right
            
        self.length += 1
            
    def popFront(self) :
        if self.head == None :
            return -1
        elif self.length == 1 :
            k = self.head.key
            self.head = None
            self.tail = None
            self.length -= 1
            return k
        else :
            k = self.head.key
            self.head = self.head.right
            self.head.left = None
            self.length -= 1
            return k
        
    def popBack(self) :
        if self.head == None :
            return -1
        elif self.length == 1 :
            k = self.head.key
            self.head = None
            self.tail = None
            self.length -= 1
            return k
        else :
            k = self.tail.key
            self.tail = self.tail.left
            self.tail.right = None
            self.length -= 1
            return k

D = Deque()

for _ in range(N) :
    R = stdin.readline().rstrip()
    
    if R[0] == "1" :
        D.PushFront(R.split()[-1])
    elif R[0] == "2" :
        D.PushBack(R.split()[-1])
    elif R == "3" :
        print(D.popFront())
    elif R == "4" :
        print(D.popBack())
    elif R == "5" :
        print(len(D))
    elif R == "6" :
        if len(D) == 0 :
            print(1)
        else :
            print(0)
    elif R == "7" :
        if len(D) == 0 :
            print(-1)
        else :
            print(D.head.key)
    else :
        if len(D) == 0 :
            print(-1)
        else :
            print(D.tail.key)