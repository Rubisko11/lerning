number = int(input())
mult = 1
for i in range (2, number):
    for a in range(2,i):
        if i % a==0:
            mult *= 0
            break
    if mult == 1:
        print (i)
    mult = 1

