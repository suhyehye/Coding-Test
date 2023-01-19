def solution(skill, skill_trees):
    answer = len(skill_trees)
    skill = {k:v for k,v in zip(skill,range(len(skill)))}
    for i in skill_trees:
        a = -1
        for j in i:
            if j in skill.keys() and skill[j] <= a+1:
                a = max(skill[j],a)
            elif j in skill.keys() and skill[j] > a:
                answer -= 1
                break
    return answer
