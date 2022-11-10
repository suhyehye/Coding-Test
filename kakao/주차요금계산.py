from datetime import datetime
import time
from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    cars = defaultdict(list)
    for i in records:
        car_info = i.split(' ')
        cars[car_info[1]].append(car_info[0]+' '+car_info[2])
    cars = dict(sorted(cars.items()))
    
    for i in cars:
        i_fee = []
        for j in range(len(cars[i])):
            if 'IN' in cars[i][j]:
                intime = datetime.strptime(cars[i][j].split(' ')[0],'%H:%M')
                try:
                    outtime=datetime.strptime(cars[i][j+1].split(' ')[0],'%H:%M')
                except:
                    outtime = datetime.strptime('23:59','%H:%M')
                i_fee.append((outtime-intime).seconds//60)
        print(i_fee,sum(i_fee)-fees[0])
        if sum(i_fee)<fees[0]:
            answer.append(fees[1])
        else:
            answer.append(int(fees[1]+math.ceil((sum(i_fee)-fees[0])/fees[2])*fees[3]))
    
    return answer
