from collections import Counter
def solution(want, number, discount):
    want_dict = dict(zip(want, number))
    want_dict = sorted(want_dict.items())
    answer = 0
    for i in range(len(discount)-9):
        if sorted(Counter(discount[i:i+10]).items()) == want_dict:
            answer += 1
            
    return answer
