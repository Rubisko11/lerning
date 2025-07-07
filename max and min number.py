number = int(input()) 
last_number = number%10
number = number//10
maximal_number = last_number
minimal_number = last_number
while number!=0:
    last_number = number%10
    if last_number > maximal_number:
        maximal_number = last_number
    elif last_number < minimal_number:
        minimal_number = last_number
    number = number//10
print('Максимальная цифра равна', maximal_number)
print('Минимальная цифра равна', minimal_number)