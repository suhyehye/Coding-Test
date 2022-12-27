def solution(n, left, right):
    answer = [[i+1 for _ in range(i+1)] + list(range(i+2,n+1)) for i in range(left//n, right//n+1)]
    return sum(answer,[])[left%n:(right//n-left//n)*n+right%n+1]
