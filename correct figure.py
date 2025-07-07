import math as m
n = int(input())
a = float(input())
area = (n*a**2)/(4*m.tan(m.pi/n))
print(area)