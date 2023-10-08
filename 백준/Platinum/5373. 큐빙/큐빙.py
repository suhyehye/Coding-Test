import sys

input = sys.stdin.readline

def move(order, d):
    global cube
    if order == 'U':
        if d == '+':
            cube[2][0], cube[5][0], cube[3][0], cube[4][0] = cube[5][0], cube[3][0], cube[4][0], cube[2][0]
        else:
            cube[2][0], cube[4][0], cube[3][0], cube[5][0] = cube[4][0], cube[3][0], cube[5][0], cube[2][0]
    
    elif order == 'D':
        if d == "-":
            cube[2][2], cube[4][2], cube[3][2], cube[5][2] = cube[5][2], cube[2][2], cube[4][2], cube[3][2]
        else:
            cube[2][2], cube[5][2], cube[3][2], cube[4][2] = cube[4][2], cube[2][2], cube[5][2], cube[3][2]
            
    elif order == 'L':
        if d == "+":        
            temp = [x[0] for x in cube[0]]
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
            cube[3][2][2], cube[3][1][2], cube[3][0][2] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = temp        
        else:
            temp = [x[0] for x in cube[0]]
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
            cube[3][2][2], cube[3][1][2], cube[3][0][2] = temp  
            
    elif order == 'R':
        if d == "+":
            temp = [x[2] for x in cube[0]]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
            cube[3][2][0], cube[3][1][0], cube[3][0][0] = temp
        else:
            temp = [x[2] for x in cube[0]]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
            cube[3][2][0], cube[3][1][0], cube[3][0][0] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = temp
                
    elif order == "F":
        if d == "+":
            temp = cube[0][2]
            cube[0][2] = [x[2] for x in cube[4]][::-1]
            cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[1][0]
            cube[1][0] = [x[0] for x in cube[5]][::-1]
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = temp
        else:
            temp = cube[0][2]
            cube[0][2] = [x[0] for x in cube[5]]
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[1][0][::-1]
            cube[1][0] = [x[2] for x in cube[4]]
            cube[4][0][2], cube[4][1][2], cube[4][2][2] = temp[::-1]
        
    elif order == 'B':
        if d == '+':
            temp = cube[0][0]
            cube[0][0] = [x[2] for x in cube[5]]
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[1][2][::-1]
            cube[1][2] = [x[0] for x in cube[4]]
            cube[4][0][0], cube[4][1][0], cube[4][2][0] = temp[::-1]
        else:
            temp = cube[0][0]
            cube[0][0] = [x[0] for x in cube[4]][::-1]
            cube[4][0][0], cube[4][1][0], cube[4][2][0] = cube[1][2]
            cube[1][2] = [x[2] for x in cube[5]][::-1]
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = temp
            
def change(i, d):
    c0, c1, c2 = cube[i][0], cube[i][1], cube[i][2]
    n_arr = [[0 for _ in range(3)] for _ in range(3)]
    if d == '+':
        n_arr[0][0], n_arr[1][0], n_arr[2][0] = c2
        n_arr[0][1], n_arr[1][1], n_arr[2][1] = c1
        n_arr[0][2], n_arr[1][2], n_arr[2][2] = c0
    else:
        n_arr[0][0], n_arr[1][0], n_arr[2][0] = reversed(c0)
        n_arr[0][1], n_arr[1][1], n_arr[2][1] = reversed(c1)
        n_arr[0][2], n_arr[1][2], n_arr[2][2] = reversed(c2)
    cube[i] = n_arr
    
T = int(input())
for _ in range(T):
    cube_d = {"U":0, "D":1, "F":2, "B":3, "L":4, "R":5}
    cube = [[['w','w','w'],['w','w','w'],['w','w','w']],
            [['y','y','y'],['y','y','y'],['y','y','y']],
            [['r','r','r'],['r','r','r'],['r','r','r']],
            [['o','o','o'],['o','o','o'],['o','o','o']],
            [['g','g','g'],['g','g','g'],['g','g','g']],
            [['b','b','b'],['b','b','b'],['b','b','b']]]
    
    n = int(input())
    arr = input().split()
    
    for i in arr:
        order, d = i[0], i[1]
        move(order, d)
        change(cube_d[order], d)
        
    for i in cube[0]:
        print("".join(i))