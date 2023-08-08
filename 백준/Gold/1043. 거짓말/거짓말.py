N, M = map(int, input().split())
p_list = set(input().split()[1:])
cnt = 0

parties = [set(input().split()[1:]) for _ in range(M)]

for _ in range(M):
    for party in parties:
        if len(party & p_list) > 0:
            p_list.update(party)

for party in parties:
    if len(party & p_list) == 0:
        cnt += 1
        
print(cnt)