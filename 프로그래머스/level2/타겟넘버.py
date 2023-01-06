def solution(numbers, target):
    visited = [numbers[0], -numbers[0]]
    for i in numbers[1:]:
        stack = visited
        visited = [x + i for x in stack]
        visited.extend([x-i for x in stack])    
    return visited.count(target)
