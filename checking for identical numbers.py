number = int(input())
mult = 1
last_number_1 = number%10
number = number // 10
while number>0:
    last_number_2 = number%10
    if last_number_2 == last_number_1:
        mult *= 1
    else:
        mult *= 0
    last_number_1 = last_number_2
    number = number // 10
if mult == 1:
    print("YES")
else :
    print("NO")
