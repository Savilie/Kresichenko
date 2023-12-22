#1 Дана строка. Подсчитать общее количество содержащихся в ней строчных латинских и русских букв.

def count_letters(text):
    latin_count = sum(1 for char in text if 'a' <= char <= 'z' or 'A' <= char <= 'Z')
    russian_count = sum(1 for char in text if 'а' <= char <= 'я' or 'А' <= char <= 'Я')
    return latin_count, russian_count

input_string = input('Введите текст без цифр на кириллице или латинице: ')
latin, russian = count_letters(input_string)
print(f"Количество латинских букв: {latin}")
print(f"Количество русских букв: {russian}")
