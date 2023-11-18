def check(k, x, y, places):
    d = [(0,1), (1,0)]
    for i in range(2):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if places[k][nx][ny] == 'P':
                return False

    if x + 1 < 5 and y+1 < 5 and places[k][x+1][y+1] == 'P':
        if places[k][x][y+1] != 'X' or places[k][x+1][y] != 'X':
            return False
    
    if x + 1 < 5 and 0 <= y - 1 < 5 and places[k][x+1][y-1] == 'P':
        if places[k][x+1][y] != 'X' or places[k][x][y-1] != 'X':
            return False
    
    if x + 2 < 5 and places[k][x+2][y] == 'P' and places[k][x+1][y] == 'O':
        return False
    
    if y + 2 < 5 and places[k][x][y+2] == 'P' and places[k][x][y+1] == 'O':
        return False
    return True
    
def solution(places):
    answer = []
    for k in range(5):
        flag = 1
        for i in range(5):
            for j in range(5):
                if places[k][i][j] == 'P':
                    if not check(k,i,j,places):
                        flag = 0
                        break
            if not flag:
                break
        answer.append(flag)
    return answer