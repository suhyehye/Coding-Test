import re
from collections import Counter
def solution(s):
    count = Counter(re.findall(r"\d+", s))
    return [int(k) for k,v in sorted(count.items(), key=lambda x:x[1], reverse=True)]