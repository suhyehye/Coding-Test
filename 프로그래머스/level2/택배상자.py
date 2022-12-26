def solution(order):
    answer = 0
    box = list(range(0,order[0]+1))
    container = [0]
    for idx,i in enumerate(order):
        if i == box[-1]:
            answer += 1
            container.append(i)
            box.pop()
        elif i == order[idx-1]+1:
            container.append(i)
            answer += 1
        elif i < box[-1]:
            return answer
        else:
            answer += 1
            box.extend(list(range(max(order[:idx-1])+1, i)))
    print(container)
    return answer
