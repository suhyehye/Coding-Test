from collections import deque
def solution(numbers):
    numbers.sort(key=lambda x: (str(x)[0],str(x)*3,str(x)[-1]),reverse=True)
    numbers = deque(numbers)
    answer = ''
    
    while len(numbers) >= 2:
        n1 = str(numbers.popleft())
        n2 = str(numbers.popleft())
        if len(n1) == 1:
            answer += n1
            numbers.appendleft(n2)
        elif n1 + n2 >= n2 + n1:
            answer += n1
            numbers.appendleft(n2)
        else:
            numbers.appendleft(n1)
            numbers.appendleft(n2)
    answer += ''.join(numbers)
    return str(int(answer))
