first_number = int(input())
second_number = int(input())
third_number = int(input())
fourth_number = int(input())
sum_1 = first_number + second_number
sum_2 = third_number + fourth_number
if sum_1%2==0 and sum_2%2==0:
    print('YES')
elif sum_1%2==1 and sum_2%2==1:
    print('YES')
else:
    print('NO')