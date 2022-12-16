from collections import Counter
def solution(topping):
    answer = 0
    s = set()
    count = Counter(topping)
    
    for i in topping:
        s.add(i)
        count[i] -= 1
        if count[i] == 0:
            count.pop(i)
        
        if len(s) == len(count):
            answer += 1
        
    return answer
