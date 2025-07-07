number = int(input()) 
count = 1
last_number_2 = number%10
sum = last_number_2
mult = last_number_2
number = number//10
while number!=0:
    last_number = number%10
    count += 1
    sum += last_number
    mult *= last_number
    number = number//10
print(sum) # сумма
print(count) # количество цифр
print(mult)# произведение
print(sum/count)# среднее арифметическое
print(last_number)# первое число
print(last_number + last_number_2)# сумма первой и последней цифры