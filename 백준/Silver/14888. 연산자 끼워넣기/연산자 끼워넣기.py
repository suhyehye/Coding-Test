from itertools import permutations
N = int(input())
nums = input().split()
op = ['+', '-', '*', '//']
op_l = list(map(int, input().split()))
operators = sum([[x] * i for x, i in zip(op, op_l)], [])

min_v, max_v = int(1e9) + 1, int(1e9) * (-1) -1

for op in set(permutations(operators, N-1)):
    temp = nums[0]
    for num, i in zip(nums[1:], op):
        if int(temp) < 0 and i == '//':
            temp = int(temp)* (-1)
            temp = eval(str(temp) + i + num) * (-1)
        else:
            temp = eval(str(temp) + i + num)
        
    min_v = min(min_v, temp)
    max_v = max(max_v, temp)
    
print(max_v)
print(min_v)