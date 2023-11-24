def remove(arr, cap):
    tmp = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] + tmp <= cap:
            tmp += arr[i]
            arr.pop()
            if i == 0:
                break
        else:
            if cap - tmp > 0:
                arr[i] -= cap - tmp
            break
    return arr
    
def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        if deliveries and deliveries[-1] == 0:
            deliveries.pop()
            continue
        if pickups and pickups[-1] == 0:
            pickups.pop()
            continue
        
        answer += max(len(deliveries), len(pickups)) * 2
        
        if deliveries : deliveries = remove(deliveries, cap)
        if pickups : pickups = remove(pickups, cap)
    return answer