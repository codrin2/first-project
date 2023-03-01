n = int(input())
stack = 0
x = 666
while stack < n:
    test = list(str(x))
    cnt = 0
    for i in test:
        if i == '6':
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            break
    if cnt == 3:
        stack += 1
        x += 1
    else:
        x += 1
print(x)
