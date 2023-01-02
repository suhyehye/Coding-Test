def solution(x):
    if int(x) % sum(list(int(x) for x in str(x))) == 0:
        return True
    else:
        return False
