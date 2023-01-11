from collections import defaultdict
def solution(genres, plays):
    dictionary = defaultdict(int)
    music = [[idx,x,y] for (idx,x),y in zip(enumerate(genres), plays)]
    for x,y in zip(genres, plays):
        dictionary[x] += y
    music.sort(key=lambda x: (dictionary[x[1]],x[2]),reverse=True)
    
    cnt = 0
    answer = [music[0][0]]
    for idx,x in enumerate(music[1:]):
        cnt += 1
        if music[idx-1][1] != x[1]:
            cnt = 1
        if cnt < 2:
            answer.append(x[0])
        
    return answer
