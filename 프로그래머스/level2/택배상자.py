def solution(order):
    answer = 0
    box = list(range(1,order[0]+1))
    for idx,i in enumerate(order):
        if len(box) == 0:
            box.append(i)
        if i == box[-1]:
            answer += 1
            box.pop()
        elif i == order[idx-1]+1:
            answer += 1
        elif i < box[-1]:
            return answer
        else:
            answer += 1
            box.extend(list(range(max(order[:idx])+1, i)))
    return answer
