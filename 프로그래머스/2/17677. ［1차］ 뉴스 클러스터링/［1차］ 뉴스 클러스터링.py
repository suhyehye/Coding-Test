import re
from collections import Counter
def solution(str1, str2):
    answer = 0
    ar1 = [str1[x:x+2].lower() for x in range(len(str1) - 1) if str1[x:x+2].isalpha()]
    ar2 = [str2[x:x+2].lower() for x in range(len(str2) - 1) if str2[x:x+2].isalpha()]
    
    if len(ar1) == 0 and len(ar2) == 0:
        return 65536
    c1 = Counter(ar1)
    c2 = Counter(ar2)
            
    return int(sum((c1&c2).values()) / sum((c1|c2).values()) * 65536)