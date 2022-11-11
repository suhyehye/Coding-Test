from itertools import combinations
def solution(number):
    answer = 0
    com = list(combinations(number,3))
    answer = len([x for x in com if sum(x) == 0])
    return answer
