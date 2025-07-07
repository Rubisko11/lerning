num = int(input())
for i in range(1, num+1):
    print('')
    for x in range (1, i+1):
        print(x, end='')
    for y in range(i-1, 0, -1):
        print(y, end='')

