def change_time(x):
    h, m = x.split(':')
    return int(h) * 60 + int(m)

def solution(m, musicinfos):
    answer = ["(None)", 0]
    m = m.replace('G#','W').replace('A#','S').replace('C#', 'X').replace('D#', 'Y').replace("F#",'Z')
    for music in musicinfos:
        s, e, name, x = music.split(',')
        s = change_time(s)
        e = change_time(e)
        time = e - s
        x = x.replace('G#','W').replace('A#','S').replace('C#', 'X').replace('D#', 'Y').replace("F#",'Z')
        x = x * ((time) // len(x)) + x[:(time)%len(x)]
        if m in x and answer[1] < time:
            answer = [name, time]
    return answer[0]