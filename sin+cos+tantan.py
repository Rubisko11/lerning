import math as m
gradus = float(input())
radiana = gradus*m.pi/180

print(m.sin(radiana) + m.cos(radiana) + (m.tan(radiana))**2)