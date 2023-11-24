import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = self
        self.right = self
    
    def __str__(self):
        return str(self.key)
        

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __iter__(self):
        v = self.head.right
        while v != self.head:
            yield v     # 객체 v를 제너레이터로 생성
            v = v.right
    def __str__(self):
        return "".join(str(v.key) for v in self)
    
    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return
        # a, b 구간 자르기
        a.left.right = b.right
        b.right.left = a.left      
        
        # a..b를 x다음에 삽입
        x.right.left = b
        b.right = x.right
        a.left = x
        x.right = a
        
    def moveAfter(self, a, x):
        self.splice(a, a, x)
        
    def moveBefore(self, a, x):
        self.splice(a, a, x.left)
    
    def insertBefore(self, a, key):
        self.moveBefore(Node(key), a)
    
    def deleteNode(self, x):
        if x == None or x == self.head:
            return
        # 노드 x를 리스트에서 분리하기
        x.left.right, x.right.left = x.right, x.left
          

if __name__ == '__main__':
    L = LinkedList()
    c = Node("|")
    c.right = L.head
    c.left = L.head
    L.head.right = c
    L.head.left = c
    x = input().rstrip()
    n = int(input())
    
    for i in x:
        L.insertBefore(c, i)

    for _ in range(n):
        cmd = input().rstrip()
        if cmd == 'L' and c.left.key!=None :
            L.moveBefore(c, c.left)
        elif cmd == 'D' and c.right.key!=None:
            L.moveAfter(c, c.right)
        elif cmd[0] == 'B' and c.left.key!= None:
            L.deleteNode(c.left)
        elif cmd[0] == "P":
            L.insertBefore(c, cmd[2])
    
    L.deleteNode(c)
    print(L)