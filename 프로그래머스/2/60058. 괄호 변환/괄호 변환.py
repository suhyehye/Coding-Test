def split_uv(p):
    l,r = 0,0
    for idx, x in enumerate(p):
        if x == '(':
            l += 1
        else:
            r += 1
        
        if l == r:
            return p[:idx+1], p[idx+1:]

def check(u):
    stack = []
    for x in u:
        if x == '(':
            stack.append(x)
        elif x == ')' and stack:
            stack.pop()
        else:
            return False
    return True

def solution(p):
    answer = ''
    
    if p == '':
        return p
    
    u, v = split_uv(p)
    if check(u):
        return u + solution(v)
    
    answer = '('
    answer += solution(v)
    answer += ')'
    u = u[1:-1]
    for x in u:
        if x == '(':
            answer += ')'
        else:
            answer += '('
            
    return answer