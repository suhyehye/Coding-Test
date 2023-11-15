from collections import defaultdict
from math import ceil
def solution(fees, records):
    answer = []
    cars = defaultdict(list)
    
    for x in records:
        t, car, k = x.split(' ')
        time = t.split(':')
        time = int(time[0]) * 60 + int(time[1])
        cars[car].append([time, k])
        
    cars = dict(sorted(cars.items()))
    
    for k, v in cars.items():
        v = sorted(v)
        tmp = 0
        for idx, x in enumerate(v):
            if x[1] == 'IN':
                if idx == len(v)-1:
                    tmp += 23*60+59 - x[0]
                else:
                    tmp += v[idx+1][0] - x[0]
        
        if tmp <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(ceil((tmp-fees[0]) / fees[2]) * fees[3]+ fees[1])
        
    return answer