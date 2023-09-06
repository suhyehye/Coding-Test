N, K = map(int, input().split())
arr = list(map(int, input().split()))

multi = []
cnt = 0
for i in range(K):
    if arr[i] in multi:
        continue
    if len(multi) < N:
        multi.append(arr[i])
        continue
    
    idx, temp = 0, 0
    for j in multi:
        if j not in arr[i:]:
            temp = j
            break
        elif arr[i:].index(j) > idx:
            idx = arr[i:].index(j)
            temp = j
    multi[multi.index(temp)] = arr[i]
    cnt += 1
             
print(cnt)