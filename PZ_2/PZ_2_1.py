#Вариант 15
#Дано трехзначное число. Вывести вначале его последнюю цифру (единицу), а затем - его среднюю цифру (десятки)


num = int(input("Введите трехзначное число: "))
if num > 99 and num < 1000:
    last_digit = num % 10
    middle_digit = (num // 10) % 10
    print("Последнее цифра", last_digit)
    print("Средняя цифра", middle_digit)
else:
    print("Введите трёхзначное число!")

