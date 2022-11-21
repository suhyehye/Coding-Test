def solution(array, commands):
    answer = []
    for i in commands:
        a = sorted(array[i[0]-1:i[1]])[i[2]-1]
        answer.append(a)
    return answer
