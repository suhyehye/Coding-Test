N = int(input())
arr = sorted(list(map(int, input().split())))

space = [0,0]
for i in arr:
    n_space = [i, space[1]+i]
    if i <= space[1] + 1:
        space[1] = n_space[1]
    else:
        break
print(space[1] + 1)