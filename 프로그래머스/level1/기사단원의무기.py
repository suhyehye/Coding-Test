def getMyDivisor(n):
    cnt = 0
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            cnt += 1
            if ( (i**2) != n) : 
                cnt += 1
    return cnt

def solution(number, limit, power):
    answer = []
    for i in range(1,number+1):
        n = getMyDivisor(i)
        if n > limit : n = power
        answer.append(n)
    return sum(answer)
