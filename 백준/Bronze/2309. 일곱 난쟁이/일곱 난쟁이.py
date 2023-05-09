from itertools import combinations

arr = []
for _ in range(9):
    arr.append(int(input()))
    
total = sum(arr)

for i in list(combinations(arr, 7)):
    total = sum(i)
    if total == 100:
        print(*sorted(i))
        break