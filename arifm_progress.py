stroka_1 = input()
stroka_2 = input()
stroka_3 = input()
leanght_of_stroka_1 = len(stroka_1)
leanght_of_stroka_2 = len(stroka_2)
leanght_of_stroka_3 = len(stroka_3)
delta_1_2 = abs(leanght_of_stroka_1-leanght_of_stroka_2)
delta_2_3 = abs(leanght_of_stroka_2-leanght_of_stroka_3)
delta_3_1 = abs(leanght_of_stroka_3-leanght_of_stroka_1)
if leanght_of_stroka_1==leanght_of_stroka_2 or leanght_of_stroka_1==leanght_of_stroka_3 or leanght_of_stroka_2==leanght_of_stroka_3:
    print('NO')
elif (delta_1_2==delta_2_3 or delta_1_2==delta_3_1) or (delta_2_3==delta_1_2 or delta_2_3==delta_3_1):
    print('YES')
else:
    print('NO')

