number = int(input())
sum = 0
for i in range(1,number+1):
    sum += (-1)**(i+1)*i
print(sum)