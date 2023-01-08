def solution(operations):
    answer = []
    for i in operations:
        if i[0] == 'I':
            answer.append(int(i[1:]))
        elif i == 'D 1' and len(answer) > 0:
            answer.pop(answer.index(max(answer)))
        elif i == 'D -1' and len(answer) > 0:
            answer.pop(answer.index(min(answer)))
    if answer == []:
        return [0,0]
    return [max(answer), min(answer)]
