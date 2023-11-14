#Дано вещественное число A и целое число N (>0).
#Используя один цикл, найти сумму 1 + A + A^2 + A^3 + ... + A^n.
try:
    A = float(input('Вещественное A: '))
    N = int(input('Целочисленное N>0: '))

    sum = 0
    power = 1
    if N>0:
        for i in range(N+1):
            sum += power
            power *= A
    else:
        exit()

    print("Сумма ряда:", sum)
except:
    print('False')