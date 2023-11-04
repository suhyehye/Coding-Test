import sys
from collections import defaultdict
input = sys.stdin.readline

arr = []
S, E, Q = input().split()

def change(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

S = change(S)
E = change(E)
Q = change(Q)

check = defaultdict(set)

while True:
    try:
        time, name = input().split()
        time = change(time)
        
        if time <= S:
            check['S'].add(name)
            
        if E <= time <= Q:
            check['E'].add(name)
    except:
        break
    
print(len(check['S'] & check['E']))