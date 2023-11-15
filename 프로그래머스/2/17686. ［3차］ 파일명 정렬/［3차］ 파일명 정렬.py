import re
def solution(files):
    f_dict = {}
    for file in files:
        mid = re.findall(r'\d+', file)
        head = file.split(mid[0])
        f_dict[file] = [head[0].lower(), int(mid[0])]
    f_dict = sorted(f_dict.items(),key=lambda x:(x[1][0],x[1][1]))
    return [x[0] for x in f_dict]