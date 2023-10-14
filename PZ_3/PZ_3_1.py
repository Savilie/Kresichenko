# Вариант 15 задание 1
# Даны три целых числа: A,B,C. Проверить истинность высказывания:
# "Ровно одно из трех чисел A,B,C положительное."

try:
    a = int(input('Введите число A:'))
    b = int(input('Введите число B:'))
    c = int(input('Введите число C:'))
    if a < 0 and b < 0 and c < 0:
        exit()
    elif a > 0 and b > 0 and c > 0:
        exit()
    elif a > 0 and b > 0:
        exit()
    elif a > 0 and c > 0:
        exit()
    elif c > 0 and b > 0:
        exit()
    else:
        print('True')
except:
    print('False')