def solution(numbers):
    numbers.sort(key=lambda x: str(x)*3,reverse=True)
    
    return str(int(''.join(list(map(str,numbers)))))
