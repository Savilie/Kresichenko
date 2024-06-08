# Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 2 - 9.

import tkinter as tk
from tkinter import messagebox

def calculate_digits():
    try:
        num = int(entry.get())
        if 99 < num < 1000:
            last_digit = num % 10
            middle_digit = (num // 10) % 10
            result_last_digit.config(text=f"Последняя цифра: {last_digit}")
            result_middle_digit.config(text=f"Средняя цифра: {middle_digit}")
        else:
            messagebox.showerror("Ошибка ввода", "Введите трёхзначное число!")
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Введите допустимое число!")


# Создание основного окна
root = tk.Tk()
root.title("Подсчет цифр")
root.resizable(False, False)
root.geometry('300x200')

# Метка и поле ввода
prompt_label = tk.Label(root, text="Введите трёхзначное число:")
prompt_label.pack(pady=15)

entry = tk.Entry(root)
entry.pack(pady=5)

# Кнопка для запуска вычислений
calculate_button = tk.Button(root, text="Вычислить", command=calculate_digits)
calculate_button.pack(pady=10)

# Метки для отображения результата
result_last_digit = tk.Label(root, text="")
result_last_digit.pack(pady=5)

result_middle_digit = tk.Label(root, text="")
result_middle_digit.pack(pady=5)

# Запуск главного цикла событий
root.mainloop()
