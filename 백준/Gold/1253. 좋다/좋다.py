import sys
input = sys.stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))

def check(i):
    temp = arr[i]
    n_arr = arr[:i] + arr[i+1:]
    start, end = 0 , len(n_arr) - 1
    
    while start < end:
        if n_arr[start] + n_arr[end] < temp:
            start += 1
        elif n_arr[start] + n_arr[end] > temp:
            end -= 1
        else:
            return 1
    return 0

ans = 0
for i in range(N):
    ans += check(i)
print(ans)