# 페르마의 소정리

# 분할 정복을 이용해 a^b를 구함
def power(a,b):
    if b == 0:
        return 1
    if b % 2:
        return (power(a, b // 2) ** 2 * a) % p
    else:
        return (power(a, b // 2) ** 2) % p

p = 1000000007
N, K = map(int, input().split())

# nCK를 나타내기 위한 팩토리얼을 dp로 구함
fact = [1 for _ in range(N+1)]

for i in range(2, N+1):
    fact[i] = fact[i-1] * i % p

# A는 nCK의 분자가 되고 B는 분모가 됨
A = fact[N]
B = (fact[N-K] * fact[K]) % p

print((A % p) * (power(B, p-2) % p) % p)