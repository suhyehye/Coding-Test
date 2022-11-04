import re
def solution(dart):
    answer = []
    nums = re.findall('\d+', dart)
    points = re.split('\d+', dart)[1:]
    points = [x.replace('S','**1').replace('D','**2').replace('T','**3') for x in points]
    
    for i in range(3):
        if points[i][-1] == '*' and i ==0:
            answer.append(eval(nums[i]+points[i][:-1]+'*2'))
            
        elif points[i][-1] == '#':
            answer.append(eval(nums[i]+points[i][:-1]+'*(-1)'))
            
        elif points[i][-1] == '*':
            answer[-1] = answer[-1]*2
            answer.append(eval(nums[i]+points[i][:-1]+'*2'))
            
        else:
            answer.append(eval(nums[i]+points[i]))
    
    return sum(answer)
