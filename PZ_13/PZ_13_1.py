# Вариант 15.
# 1.	В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
#       Выполнить замену элементов второй строки исходной матрицы на полученные суммы.
# 2.	В матрице найти минимальный элемент в предпоследней строке.


import random


matrix = [[random.randint(-8, 8) for i in range(4)] for i in range(4)]

print("Исходная матрица:")
for i in matrix:
    print(i)


# нужно использовать lambda

column_sums = list(map(lambda j: sum(row[j] for row in matrix), range(len(matrix[0]))))
print("Суммы элементов каждого столбца (lambda):", column_sums)

matrix[1] = column_sums

print("Итоговая матрица:")
for i in matrix:
    print(i)

print("Минимальный элемент в предпоследней строке:", min(matrix[-2]))