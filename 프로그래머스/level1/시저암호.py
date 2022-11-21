def solution(s, n):
    list_lower = [chr(i) for i in range(97,123)] * 2
    list_upper = [chr(i) for i in range(65, 91)] * 2
    answer = ''

    for i in s:
        if ord(i) in range(97, 123):
            answer = answer + list_lower[list_lower.index(i)+n]
        elif i == ' ':
            answer = answer + " "
        else:
            answer = answer + list_upper[list_upper.index(i)+n]
    return answer
