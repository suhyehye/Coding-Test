N, K = map(int, input().split())
arr = sorted(list(map(int, input().split())))

dist = sorted([y-x for x,y in zip(arr[:N-1], arr[1:])])
print(sum(dist[:N-K]))