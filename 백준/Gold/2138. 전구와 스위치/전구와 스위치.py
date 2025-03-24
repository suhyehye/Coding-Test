n = int(input())
brights = list(map(int, input()))
gt = list(map(int, input()))

def search(cnt, brights, gt):
    for i in range(1, n-1):
        if brights[i-1] != gt[i-1]:
            brights[i-1] = (brights[i-1] + 1) % 2
            brights[i] = (brights[i] + 1) % 2
            brights[i+1] = (brights[i+1] + 1) % 2
            cnt += 1
    
    if brights[n-2] != gt[n-2]:
        brights[n-1] = (brights[n-1] + 1) % 2
        brights[n-2] = (brights[n-2] + 1) % 2
        cnt += 1
    
    if brights[n-1] != gt[n-1]:
        cnt = -1
    return cnt

# 첫번째 스위치를 누르는 경우
brights_0 = brights.copy()
brights_0[0] = (brights_0[0] + 1) % 2
brights_0[1] = (brights_0[1] + 1) % 2
cnt0 = search(1, brights=brights_0, gt=gt)

# 첫번째 스위치를 누르지 않는 경우
cnt1 = search(0, brights=brights.copy(), gt=gt)

print(min(cnt0, cnt1) if cnt1 != -1 and cnt0 != -1 else max(cnt0, cnt1))