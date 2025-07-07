import math as m
number = int(input())
sum = 0
for i in range(1,1+number):
    sum += 1/i
print(sum-m.log(number))