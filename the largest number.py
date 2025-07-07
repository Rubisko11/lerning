quant = int(input())
largest_number = 0
second_largest_number = 0
for i in range(1,quant+1):
    number = int(input())
    if number>largest_number:
        second_largest_number = largest_number
        largest_number = number

    elif number>largest_number:
        largest_number = number
    else:
        second_largest_number = number 
print(largest_number)
print(second_largest_number)