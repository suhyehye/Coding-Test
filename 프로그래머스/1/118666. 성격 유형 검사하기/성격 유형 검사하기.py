from collections import defaultdict
def solution(survey, choices):
    scores = defaultdict(int)
    for s, choice in zip(survey, choices):
        if choice < 4:
            scores[s[0]] += 4 - choice
        elif choice > 4:
            scores[s[1]] += choice - 4
            
    mbti = [['R','T'], ["C","F"], ["J","M"], ["A","N"]]
    answer = ''
    for i in range(4):
        if scores[mbti[i][0]] < scores[mbti[i][1]]:
            answer += mbti[i][1]
        else:
            answer += mbti[i][0]
    return answer