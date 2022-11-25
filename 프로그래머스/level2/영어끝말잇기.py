def solution(n, words):
    answer = [words[0][0]]
    for idx,i in enumerate(words):
        if i not in answer and answer[-1][-1] == i[0]:
            answer.append(i)
        else:
            return [idx%n+1, idx//n+1]
    return [0,0]
