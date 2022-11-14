def solution(sizes):
    sizes = [sorted(x, reverse=True) for x in sizes]
    
    answer = max([x[0] for x in sizes]) * max([x[1] for x in sizes])
    return answer
