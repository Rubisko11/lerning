
a = float(input())
b = float(input())
c = float(input())
disc = b**2 - 4*a*c
x1 = ((-b+disc**0.5)/(2*a))
x2 = ((-b-disc**0.5)/(2*a))
if disc<0:
    print('Нет корней')
elif disc==0:
    print(x1)
else:
    print(min(x2, x1))
    print(max(x2, x1))