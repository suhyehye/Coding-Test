x = input().rstrip()

if x[0] == '-':
    x = x[1:].split('-')
    answer = sum(list(map(int, x[0].split('+')))) * (-1)
else:
    x = x.split('-')
    answer = sum(list(map(int, x[0].split('+'))))

if len(x) == 1:
    print(answer)
    exit()
    
for i in x[1:]:
    answer -= sum(list(map(int,i.split('+'))))
print(answer)