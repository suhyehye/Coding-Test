def solution(s):
    res = ""
    digit = {"zero" : "0", "one": "1", "two": "2",
            "three" : "3", "four" : "4", "five" : "5",
            "six" : "6", "seven" : "7", "eight" : "8",
            "nine" : "9"}
    
    tmp = ""
    for i in s:
        if i.isdigit():
            res += i
            continue
            
        tmp += i
        if tmp in digit.keys():
            res += digit[tmp]
            tmp = ""
            
    return int(res)