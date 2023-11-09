start = list(input().rstrip())
end = list(input().rstrip())

def find(a, b):
    if len(a) == len(b):
        return a == b

    if b[0] == "B" :
        if find(a, b[:0:-1]):
            return True
    
    if b[-1] == 'A':
        if find(a, b[:-1]):
            return True
        
print(1) if find(start, end) else print(0)