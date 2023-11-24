def solution(cap, n, deliveries, pickups):
    answer = 0
    tmp = 0
    while deliveries or pickups:
        if deliveries and deliveries[-1] == 0:
            deliveries.pop()
            continue
        if pickups and pickups[-1] == 0:
            pickups.pop()
            continue
        
        answer += max(len(deliveries), len(pickups)) * 2
        
        for i in range(len(deliveries)-1, -1, -1):
            if deliveries[i] + tmp <= cap:
                tmp += deliveries[i]
                deliveries.pop()
                if i == 0:
                    break
            else:
                if cap - tmp > 0:
                    deliveries[i] -= cap - tmp
                break
                

        tmp = 0
        
        for i in range(len(pickups)-1, -1, -1):
            if pickups[i] + tmp <= cap:
                tmp += pickups[i]
                pickups.pop()
                if i == 0:
                    break
            else:
                if cap - tmp > 0:
                    pickups[i] -= cap - tmp
                break
        tmp = 0
    
    return answer