# A = int(input("введите число"))
# B = int(input("введите число"))
# C = int(input("введите число"))
# D = int(input("введите число"))
# if A = 0
#     print("Ноль не подходит")
# if B = 0
#     print("Ноль не подходит")
# if C = 0
#     print("Ноль не подходит")

# mid_num = (A + B + C + D)/4
# print(round(mid_num,2))

# kol = 0 

# a = int(input("введите число "))
# kol = kol + 1

# sum = 0

# while a !=0:
#     print("вы ввели" kol "чисел")
#     sum = sum + a
#     print("сумма чисел равна",sum)
#     print("цикл продолжается")
#     a = int(input("Введите число A "))
#     kol = kol + 1   
 
letter = input("Введи любую латинскую букву ")
if letter.lower() in ['a','e','i','o','u']:
    print("Это гласная буква")
elif letter.lower() == 'y':
    print("Это буква может быть гласной и согласной")
else:
    print("это согласная буква")
