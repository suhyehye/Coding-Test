import math
from itertools import permutations

def primenumber(x):
    if x == 0 or x == 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    n = len(numbers)
    numbers = [str(x) for x in numbers]
    nums = []
    for i in range(1, n+1):
        nums += list(permutations(numbers, i))
    nums = [int(("").join(p)) for p in nums]

    for i in set(nums):
        if i == '0':
            break
        elif primenumber(i):
            answer += 1
        
    return answer