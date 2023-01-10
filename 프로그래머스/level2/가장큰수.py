from itertools import permutations
def solution(numbers):
    answer = list(permutations(numbers,len(numbers)))
    answer = max([''.join(map(str, x)) for x in answer])
    return answer
