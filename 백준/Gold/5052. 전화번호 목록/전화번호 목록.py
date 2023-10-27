import sys
from collections import defaultdict
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.childeren = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.childeren:
                curr_node.childeren[char] = Node(char)
            # 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.childeren[char]
        # 문자열이 끝난 지점의 노드의 data값에 해당 문자열을 입력
        curr_node.data = string
        
    # 문자열이 존재하는 지 search
    def search(self, string):
        # 가장 아래의 노드 부터 탐색 시작
        curr_node = self.head
        for s in string:
            curr_node = curr_node.childeren[s]
            
        # 탐색이 끝난 후 해당 노드의 data값이 존재한다면 문자가 포함되어 있다는 뜻
        if curr_node.childeren: 
            return False
        else:    
            return True
    
t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    nums = []
    
    for _ in range(n):
        num = input().rstrip()
        nums.append(num)
        trie.insert(num)
    
    flag = "YES"
    nums.sort()
    
    for num in nums:
        if not trie.search(num):
            flag = "NO"
            break
    print(flag)