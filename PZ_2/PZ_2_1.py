num = int(input("Введите трехзначное число"))

last_digit = num % 10

middle_digit = (num // 10) % 10

print("Последнее цифра", last_digit)
print("Средняя цифра", middle_digit)