a = int(input()) 
sum = 0
while a>0:
    if a > 24:
        a -=25
        sum += 1
    elif a > 9:
        a -= 10
        sum += 1
    elif a > 4:
        a -= 5
        sum += 1
    else:
        a -= 1
        sum += 1
print(sum)