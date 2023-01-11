from math import factorial
def solution(n, k):
    answer = []
    waiting = list(range(1,n+1))
    fac = factorial(n)
    k -= 1
    while n >= 1:
        fac = int(fac / n)
        n -= 1
        ans = waiting.pop(k//fac)
        answer.append(ans)
        k = k%fac
    return answer
