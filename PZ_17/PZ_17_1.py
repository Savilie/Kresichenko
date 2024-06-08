# Задание 1. В соответствии с номером варианта перейти по ссылке на прототип.
# Реализовать его в IDE PyCharm Community с применением пакета tk.
# Получить интерфейс максимально приближенный к оригиналу (см. таблицу 1).
# Вариант 15 - https://www.webasyst.ru/wa-data/public/updates/img/09/209/7355/7355.970.jpg
import tkinter as tk
from tkinter import ttk

# Создание основного окна
root = tk.Tk()
root.title("Создайте заказ")

root.resizable(False, False)  # Блокировка изменения размера окна
root.geometry('550x750')  # Установка размеров окна

# Создание заголовка
title_frame = tk.Frame(root, bg='#00838F', bd=10)
title_frame.pack(fill=tk.X)

title_label = tk.Label(title_frame, text="Создайте заказ", font=("Arial", 24), bg='#00838F', fg='white')
title_label.pack()

# Секция 1: Информация о заказе
section1_frame = tk.Frame(root, bd=10)
section1_frame.pack(fill=tk.X, pady=10)

section1_label = tk.Label(section1_frame, text="1 Информация о заказе", font=("Arial", 14))
section1_label.grid(row=0, column=0, columnspan=2, pady=10)

order_num_label = tk.Label(section1_frame, text="Номер заказа *")
order_num_label.grid(row=1, column=0, sticky=tk.W, pady=5)
order_num_entry = tk.Entry(section1_frame)
order_num_entry.grid(row=1, column=1, pady=5)

product_name_label = tk.Label(section1_frame, text="Название товара *")
product_name_label.grid(row=2, column=0, sticky=tk.W, pady=5)
product_name_entry = tk.Entry(section1_frame)
product_name_entry.grid(row=2, column=1, pady=5)

quantity_label = tk.Label(section1_frame, text="Количество *")
quantity_label.grid(row=3, column=0, sticky=tk.W, pady=5)
quantity_entry = tk.Entry(section1_frame)
quantity_entry.grid(row=3, column=1, pady=5)

# Секция 2: Контактная информация
section2_frame = tk.Frame(root, bd=10)
section2_frame.pack(fill=tk.X, pady=10)

section2_label = tk.Label(section2_frame, text="2 Контактная информация", font=("Arial", 14))
section2_label.grid(row=0, column=0, columnspan=2, pady=10)

name_label = tk.Label(section2_frame, text="Ваше имя")
name_label.grid(row=1, column=0, sticky=tk.W, pady=5)
name_entry = tk.Entry(section2_frame)
name_entry.grid(row=1, column=1, pady=5)

email_label = tk.Label(section2_frame, text="Ваш email *")
email_label.grid(row=2, column=0, sticky=tk.W, pady=5)
email_entry = tk.Entry(section2_frame)
email_entry.grid(row=2, column=1, pady=5)

phone_label = tk.Label(section2_frame, text="Ваш телефон *")
phone_label.grid(row=3, column=0, sticky=tk.W, pady=5)
phone_entry = tk.Entry(section2_frame)
phone_entry.grid(row=3, column=1, pady=5)
phone_hint_label = tk.Label(section2_frame, text="Формат: +7 (999) 999-99-99")
phone_hint_label.grid(row=4, column=1, sticky=tk.W, pady=5)

# Секция 3: Информация о доставке
section3_frame = tk.Frame(root, bd=10)
section3_frame.pack(fill=tk.X, pady=10)

section3_label = tk.Label(section3_frame, text="3 Информация о доставке", font=("Arial", 14))
section3_label.grid(row=0, column=0, columnspan=2, pady=10)

address_label = tk.Label(section3_frame, text="Адрес *")
address_label.grid(row=1, column=0, sticky=tk.W, pady=5)
address_entry = tk.Text(section3_frame, height=4, width=40)
address_entry.grid(row=1, column=1, pady=5)

delivery_time_label = tk.Label(section3_frame, text="Время доставки")
delivery_time_label.grid(row=2, column=0, sticky=tk.W, pady=5)

time_frame = tk.Frame(section3_frame)
time_frame.grid(row=2, column=1, pady=5)
hour_spinbox = ttk.Spinbox(time_frame, from_=0, to=23, width=2, wrap=True, state="readonly", justify=tk.CENTER, format="%02.0f")
hour_spinbox.grid(row=0, column=0)
minute_spinbox = ttk.Spinbox(time_frame, from_=0, to=59, width=2, wrap=True, state="readonly", justify=tk.CENTER, format="%02.0f")
minute_spinbox.grid(row=0, column=1)

# Кнопка "Подтвердить"
button_frame = tk.Frame(root, bd=10)
button_frame.pack(fill=tk.X, pady=10)

submit_button = tk.Button(button_frame, text="Подтвердить", font=("Arial", 14))
submit_button.pack()

root.mainloop()