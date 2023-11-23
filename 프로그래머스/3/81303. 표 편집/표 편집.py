class ListNode:
    def __init__(self, x):
        self.up = x - 1 if x -1 >= 0 else None
        self.down = x + 1
        self.state = 1
        
def solution(n, k, cmd):
    data = [ListNode(x) for x in range(n)]
    data[-1].down = None
    stack = []  # 삭제된 인덱스를 담을 스택
    
    for c in cmd:
        if c == 'C':
            stack.append(k)
            data[k].state = 0
            if data[k].up is not None:
                data[data[k].up].down = data[k].down
                
            if data[k].down is not None:
                data[data[k].down].up = data[k].up
            
            k = data[k].up if data[k].down is None else data[k].down
            
        elif c == 'Z':
            x = stack.pop()
            data[x].state = 1
            if data[x].up is not None:
                data[data[x].up].down = x
            if data[x].down is not None:
                data[data[x].down].up = x
        
        elif c[0] == 'U':
            cnt = int(c[2:])
            for i in range(cnt):
                k = data[k].up
        
        elif c[0] == 'D':
            cnt = int(c[2:])
            for i in range(cnt):
                k = data[k].down
    
    ans = ''
    for i in range(n):
        if data[i].state:
            ans += 'O'
        else:
            ans += 'X'
            
    return ans