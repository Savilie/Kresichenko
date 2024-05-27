# 1. В последовательности на n целых чисел найти и вывести:
    # 1.	максимальный среди положительных
    # 2.	минимальный среди отрицательных
    # 3.	произведение элементов

import math


li = [i for i in range(-10, 11)]

maximum = lambda n: max(n)

minimum = lambda n: min(n)

mult = lambda n: math.prod([i for i in n if i!=0])

print(li)

print(maximum(li))

print(minimum(li))

print(mult(li))


# 2.Составить генератор (yield), который выводит из строки только буквы.

def get_words(some_string):
    for i in some_string:
        if 'a' <= i <= 'z' or 'а' <= i <= 'я' or 'A' <= i <= 'Z' or 'А' <= i <= 'Я':
            yield i


print(''.join([i for i in get_words("DdAa1256SsЯя")]))
