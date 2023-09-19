number = int(input("Введите целое число, большее 999: "))

hundreds_digit = (number // 100) % 10

print(hundreds_digit)

print("Цифра в разряде сотен:", hundreds_digit)