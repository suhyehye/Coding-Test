from math import factorial
def solution(n, k):
    answer = []
    waiting = list(range(1,n+1))
    k -= 1
    while n >= 1:
        n -= 1
        fac = factorial(n)
        ans = waiting.pop(k//fac)
        answer.append(ans)
        k = k%fac
    return answer
