# 내 풀이 방법
def solution(s):
    s = s[0].upper()+s[1:].lower()
    for i in range(len(s)-1):
        if s[i] == ' ':
            s = s[:i+1] + s[i+1].upper() + s[i+2:]
    return s


# 다른 사람 풀이
def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])
