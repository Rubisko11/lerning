first_number = int(input())
second_number = int(input())
counter = 0
for i in range(first_number, second_number+1):
    if (i**3)%10==4 or (i**3)%10==9:
        counter += 1

print(counter)

    