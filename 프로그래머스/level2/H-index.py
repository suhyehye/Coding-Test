def solution(citations):
    for i in range(len(citations),-1, -1):
        new = len(list(filter(lambda x: x >=i, citations)))
        if new >= i and len(citations) - new <= i:
            return i
