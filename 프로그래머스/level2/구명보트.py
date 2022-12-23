from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while len(people) >= 1:
        i = people.pop()
        if len(people) == 0:
            answer += 1
            return answer
        elif i + people[0] <= limit:
            answer += 1
            people.popleft()
        else:
            answer += 1
        
    return answer
