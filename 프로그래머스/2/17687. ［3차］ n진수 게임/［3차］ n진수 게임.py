def convert(number, base):
    strings = "0123456789ABCDEFGH"
    result = ""
    
    while 0 < number:
        digit = number % base
        result = strings[digit] + result
        number = number // base
    return str(result)

def solution(n, t, m, p):
    answer = '0'
    cnt = 0
    while len(answer) <= t * m + p:
        answer += convert(cnt, n)
        cnt += 1
    res = ''
    for i in range(t):
        res += answer[m*i+p-1]
    return res