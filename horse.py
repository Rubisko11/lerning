a=int(input())
b=int(input())
c=int(input())
d=int(input())
delta_1 = abs(a-c)
delta_2 = abs(b-d)
if (delta_1 == 2 and delta_2 == 1) or (delta_1 == 1 and delta_2 == 2):
    print('YES')
else:
    print('NO')