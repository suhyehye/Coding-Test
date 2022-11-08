def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        ans = format(i|j, 'b').zfill(n)
        ans = ans.replace('1', '#')
        ans = ans.replace('0', ' ')
        answer.append(ans)
    return answer
