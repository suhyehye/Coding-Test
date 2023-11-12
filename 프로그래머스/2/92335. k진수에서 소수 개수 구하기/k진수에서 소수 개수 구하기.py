import math
def convert(n, k):
    tmp = ''
    while n:
        tmp += str(n % k)
        n = n // k
    return tmp[::-1]

def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
    	if x % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
        	return False
    return True	
    
def solution(n, k):
    answer = 0
    tmp = convert(n, k)
    t_list = tmp.split('0')

    for t in t_list:
        if t == '1' or t == '':
            continue
        if primenumber(int(t)):
            answer += 1
    return answer