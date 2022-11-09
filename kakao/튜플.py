import re
from collections import Counter
def solution(s):
    s = re.split('{|}|,',s)
    s = [re.sub(r'[^0-9]', '', x) for x in s if x and x != ',']
    s = Counter(s)
    s = sorted(s.items(), key=lambda i: i[1], reverse=True)
    return [int(x[0]) for x in s]
