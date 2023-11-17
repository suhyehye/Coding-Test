from collections import defaultdict
def solution(gems):
    n = len(set(gems))
    answer = [1, len(gems)]
    end = 0
    gem_dict = defaultdict(int)
    
    for start in range(len(gems)):
        while end < len(gems) and len(gem_dict) < n:
            gem_dict[gems[end]] += 1
            end += 1
        if len(gem_dict) == n and answer[1] - answer[0] > end - start - 1:
            answer = [start+1, end]
        
        gem_dict[gems[start]] -= 1
        if gem_dict[gems[start]] == 0:
            gem_dict.pop(gems[start])
    return answer