from collections import Counter
def change(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def solution(n, t, m, timetable):
    timetable = sorted([change(x) for x in timetable])
    time = 9 * 60
    for i in range(n-1):
        tmp = []
        while timetable:
            if timetable[0] <= time and len(tmp) < m:
                tmp.append(timetable.pop(0))
            if len(tmp) >= m or timetable[0] > time:
                break
        time += t
    
    timetable = [x for x in timetable if x <= time]
    if len(timetable) < m:
        ans = time
    else:
        count = Counter(timetable)
        ans = 0
        cnt = 0
        for k, v in count.items():
            cnt += v
            if cnt >= m:
                ans = k - 1
                break
            
            
    return str(ans//60).zfill(2) + ":" + str(ans%60).zfill(2)