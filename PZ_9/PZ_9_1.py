# Сгенерировать словарь вида {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216},
# удалить из него первый и последний элементы. Отобразить исходный и получившийся словарь. Использовать for, range.


dicthe = {}
for i in range(7):
    dicthe[i] = i**3

old_dict = dicthe.copy()

del dicthe[0]
del dicthe[6]

print(old_dict)
print(dicthe)



