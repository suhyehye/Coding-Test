from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = bridge_length
    q = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    b_weight = 0
    
    while len(q):
        n = q.popleft()
        b_weight -= n
        if len(truck_weights) == 0:
            break
        
        elif b_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            b_weight += truck
            q.append(truck)
        else:
            q.append(0)
        answer += 1
            
    return answer
