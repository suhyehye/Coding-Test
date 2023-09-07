N = int(input())
arr = [i for i in range(1, N+1)]

x, temp = 0, 0
while len(arr) > 1:
    x += 1
    temp += (x**3 - 1) % len(arr)
    if temp >= len(arr):
        temp -= len(arr)
    arr.pop(temp)

print(arr[-1])