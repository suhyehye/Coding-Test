N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split())))

if K >= N:
    print(0)
else :
    dist = []
    for i in range(N-1):
        dist.append(abs(arr[i+1]-arr[i]))
        
    dist.sort(reverse=True)

    for _ in range(K-1):
        dist.pop(0)
        
    print(sum(dist))