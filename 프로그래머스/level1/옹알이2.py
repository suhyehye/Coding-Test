def solution(babbling):
    answer = 0
    b_list = ["aya", "ye", "woo", "ma"]
    b_list2 = [x*2 for x in b_list]
    for b in babbling:
        for word in b_list2:
            if word in b:
                break
        else:
            for word2 in b_list:
                b = b.replace(word2,' ')
            if b.strip() == '':
                answer += 1
    return answer
