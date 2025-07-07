number = int(input()) 
sum_2 = ''
while number!=0:
    last_number = number%10
    number = number//10
    sum = str(last_number)
    sum_2 +=  sum
print(sum_2)