# Дан список A размера N. Вывести его элементы в следующем порядке: A1, An, А2, An-1, А3, An-2, ...
def print_elements_in_pattern(List):
    left = 0
    right = len(A) - 1

    while left <= right:
        if left == right:
            print(A[left])
        else:
            print(A[left], A[right], end=' ')
        left += 1
        right -= 1

A = list(input('Введите числа без запятых и пробелов: '))
print_elements_in_pattern(A)
