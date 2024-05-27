# 1.	Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Умножаем все элементы на первый элемент:


# Генерируем последовательность случайных целых чисел
import random

sequence = [64, -99, 87, 9, 57, 48, -84, -99, -98, -9]

with open('numbers.txt', 'w', encoding='utf-16') as file:
    file.write(' '.join(map(str, sequence)))

# Находим индекс последнего минимального элемента

new_sequence = [i for i in sequence]
new_sequence.pop(sequence.index(min(sequence)))

for i in range((sequence.index(min(sequence)) + 1), len(sequence)):
    if sequence[i] == min(sequence):
        min_index = new_sequence.index(min(new_sequence)) + 1
    else:
        min_index = sequence.index(min(sequence))


# Умножаем все элементы на первый элемент
multiplied_sequence = [elem * sequence[0] for elem in sequence]

# Записываем данные в новый текстовый файл
with open('processed_sequence.txt', 'w', encoding='utf-16') as file:
    file.write(f"Исходные данные: {sequence}\n")
    file.write(f"Количество элементов: {len(sequence)}\n")
    file.write(f"Индекс последнего минимального элемента: {min_index}\n")
    file.write("Умножаем все элементы на первый элемент:\n")
    for element in multiplied_sequence:
        file.write(f"{element}\n")


# 2.    Из предложенного текстового файла (text18-15.txt) вывести на экран его содержимое, количество букв в нижнем регистре.
# Сформировать новый файл, в который поместить текст в стихотворной форме предварительно заменив символы нижнего регистра на верхний.

# Чтение содержимого файла
with open('text18-15.txt', 'r', encoding='utf-16') as file:
    content = file.read()

# Подсчет количества букв в нижнем регистре
lowercase_count = sum(1 for char in content if char.islower())

# Замена символов нижнего регистра на верхний и сохранение в новый файл
content_uppercase = content.upper()
with open('new_text.txt', 'w', encoding='utf-16') as new_file:
    new_file.write(content_uppercase)

# Вывод содержимого и количества букв в нижнем регистре
print(content)
print(f"Количество букв в нижнем регистре: {lowercase_count}")