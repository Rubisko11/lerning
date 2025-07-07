import math as m
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
delta_x = abs(x2-x1)
delta_y = abs(y2-y1)
rast = m.sqrt(delta_y**2 + delta_x**2)
print(rast)
