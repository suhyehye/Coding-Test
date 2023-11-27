def check(x, y, a):
    if a == 0:
        if y == 0 or [x,y-1,0] in res or [x,y,1] in res or [x-1,y,1] in res:
            return 1
    else:
        if [x,y-1,0] in res or [x+1,y-1,0] in res or ([x-1,y,1] in res and [x+1,y,1] in res):
            return 1
    return 0

def solution(n, build_frame):
    global res
    res = []
    
    for x, y, a, b in build_frame:
        if b:
            if check(x,y,a):
                res.append([x,y,a])
        else:
            res.remove([x,y,a])
            for nx,ny,na in res:
                if not check(nx,ny,na):
                    res.append([x,y,a])
                    break
    return sorted(res)