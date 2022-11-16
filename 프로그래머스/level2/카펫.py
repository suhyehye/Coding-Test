import math
def solution(brown, yellow):
    total = brown + yellow
    x = math.ceil(math.sqrt(total))
    
    while x <= total:
        if total % x == 0 and (x-2)*(total/x-2) == yellow:
            return sorted([total/x, x], reverse=True)
        else:
            x += 1
