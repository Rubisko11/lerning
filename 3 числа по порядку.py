number = int(input())
first_number = number%10
third_number = number//100
second_number = number//10 - 10*third_number
maximal = max(first_number, second_number, third_number)
minimal = min(first_number, second_number, third_number)
medial = first_number + third_number + second_number - maximal - minimal
if maximal - minimal == medial:
    print('Число интересное')
else:
    print('Число неинтересное')
    

