def change_time(x):
    h, m = x.split(':')
    return int(h) * 60 + int(m)

def solution(m, musicinfos):
    answer = ["(None)", 0]
    m = m.replace('G#','g').replace('A#','a').replace('C#', 'c').replace('D#', 'd').replace("F#",'f')
    for music in musicinfos:
        s, e, name, x = music.split(',')
        s = change_time(s)
        e = change_time(e)
        time = e - s
        x = x.replace('G#','g').replace('A#','a').replace('C#', 'c').replace('D#', 'd').replace("F#",'f')
        x = x * ((time) // len(x)) + x[:(time)%len(x)]
        if m in x and answer[1] < time:
            answer = [name, time]
    return answer[0]