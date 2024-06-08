# 2. Дан целочисленный список размера N, все элементы которого упорядочены (по возрастанию или по убыванию).
# Найти количество различных элементов в данном списке.

list2 = []
list3 = []

def sorted(list1):
    for i in list1:
        if i % 2 == 1:
            list2.append(i)
        else:
            list3.append(i)

    print(list2, list3)

try:
    list1 = list(map
                 (int,
                     input('Введите ряд чисел без запятых через пробел: ').split()
                     )
                 )
    sorted(list1)
except:
    print('Проверьте правильность написания чисел')
