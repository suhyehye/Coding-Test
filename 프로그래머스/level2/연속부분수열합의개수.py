def solution(elements):
    answer = []
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            new_ele = elements + elements[:i-1]
            answer.append(sum(new_ele[j:j+i]))
    return len(set(answer))
