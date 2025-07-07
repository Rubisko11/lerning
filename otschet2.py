first_number = int(input())
second_number = int(input())
for i in range(first_number, second_number+1):
    if i%10==9 or i%17==0 or i%15==0:
        print(i)