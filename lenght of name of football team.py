name_of_city_1 = input()
name_of_city_2 = input()
name_of_city_3 = input()
leanght_of_city_1 = len(name_of_city_1)
leanght_of_city_2 = len(name_of_city_2)
leanght_of_city_3 = len(name_of_city_3)
long_name = max(leanght_of_city_1, leanght_of_city_2, leanght_of_city_3)
short_name = min(leanght_of_city_1, leanght_of_city_2, leanght_of_city_3)
if leanght_of_city_1==short_name:
    second_name = name_of_city_1
elif leanght_of_city_2==short_name:
    second_name = name_of_city_2
else:
    second_name = name_of_city_3

if leanght_of_city_1==long_name:
    first_name = name_of_city_1
elif leanght_of_city_2==long_name:
    first_name = name_of_city_2
else:
    first_name = name_of_city_3

print(second_name)
print(first_name)

