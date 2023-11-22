# 시계방향으로 90도 회전하는 함수
def rotate(keys, m):
    n_keys = [(y, m-x) for x, y in keys]
    return sorted(n_keys, key=lambda x:x[0])

def solution(key, lock):
    n, m = len(lock), len(key)  # 각각의 길이
    
    removes = []    # 빈 곳을 채워야 하는 lock
    for i in range(n):
        for j in range(n):
            if not lock[i][j]:
                removes.append((i,j))
    
    keys = []   # key의 돌기 부분
    for i in range(m):
        for j in range(m):
            if key[i][j]:
                keys.append((i,j))
    
    for _ in range(4):
        for i in range(-m, n):
            for j in range(-m, n):
                n_keys = [(x+i, y+j) for x,y in keys]
                tmp = 0
                flag = 0
                for x, y in n_keys:
                    if x < 0 or x >= n or y < 0 or y >= n:
                        continue
                    if (x,y) in removes:
                        tmp += 1
                    else:
                        flag = 1
                        break
                if tmp == len(removes) and not flag:
                    return True
        keys = rotate(keys,m)
    
    return False