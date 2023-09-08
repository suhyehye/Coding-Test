s = input()
t = input()

while s!=t:
    if len(t) == 0:
        print(0)
        exit()
    if t[-1] == "A":
        t = t[:-1]
    elif t[-1] == "B" :
        t = t[:-1][::-1]
    
print(1)