n = int(input())
ans = [0] * 10
num = 1

def one_digit(number):
    # 일의 자리를 9로 맞춰줌
    while number % 10 != 9:
        for i in str(number):
            ans[int(i)] += num
        number -= 1
    return number
    
while n> 0:
    n = one_digit(n)
    if n < 10:
        for i in range(n+1):
            ans[i] += num
    else:
        for j in range(10):
            ans[j] += (n // 10 + 1) * num
            
    ans[0] -= num
    num *= 10
    n //= 10

print(*ans)