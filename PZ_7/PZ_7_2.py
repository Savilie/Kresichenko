#2 Дана строка-предложение на русском языке. Подсчитать количество содержащихся в строке знаков препинания.

def count_punctuation_marks(text):
    punctuation_marks = ".,?!:;—-"
    count = sum(1 for char in text if char in punctuation_marks)
    return count

input_string = input('Введите предложение: ')
punctuation_count = count_punctuation_marks(input_string)
print(f"Количество знаков препинания: {punctuation_count}")
