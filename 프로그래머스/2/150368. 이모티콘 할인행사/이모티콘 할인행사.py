from itertools import product
def solution(users, emoticons):
    answer = []
    sales = (10, 20, 30, 40)
    answer = [0, 0]
    for p in list(product(sales, repeat = len(emoticons))):
        p_tmp = [0, 0]
        for user in users:
            tmp = 0
            for i, j in zip(p, emoticons):
                if i >= user[0]:
                    tmp += (100 - i) / 100 * j
            if tmp >= user[1]:
                p_tmp[0] += 1
            else:
                p_tmp[1] += tmp
                
        if p_tmp[0] > answer[0]:
            answer = p_tmp
        if p_tmp[0] == answer[0] and p_tmp[1] > answer[1]:
            answer = p_tmp
                
        
    return answer