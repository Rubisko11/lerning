a=int(input())
b=int(input())
c=int(input())
d=int(input())
delta_1 = abs(a-c)
delta_2 = abs(b-d)
if (a==c and   b!=d) or (a!=c and b==d):
    print('YES')
elif delta_1 == delta_2:
    print('YES')
else:
    print('NO')