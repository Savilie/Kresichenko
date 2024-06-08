# Задание 3.
# Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13), оформленный согласно требованиям.
# Все задания выполняются c использованием модуля OS:
#     перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена вложенных подкаталогов выводить не нужно.
#     перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку testl. В папку test переместить два файла из ПЗ6, а в папку testl - один файл из ПЗ7. Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере файлов в папке test.
#     перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в консоль. Использовать функцию basename () os.path.basename().
#     перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в привязанной к нему программе. Использовать функцию os.startfile().
#     удалить файл test.txt.


import os

# Функция для безопасного перемещения в каталог
def safe_chdir(directory):
    if os.path.exists(directory) and os.path.isdir(directory):
        os.chdir(directory)
    else:
        print(f"Каталог {directory} не существует или не является директорией.")
        return False
    return True

# Функция для копирования файлов
def copyfile(src, dest):
    with open(src, 'rb') as fsrc:
        with open(dest, 'wb') as fdest:
            while True:
                buf = fsrc.read(1024)
                if not buf:
                    break
                fdest.write(buf)

# Предполагаем, что текущий каталог это НЕ корневой каталог проекта 'Kresichenko'.
os.chdir('..')
current_directory = os.getcwd()

# Перейти в каталог PZ_11 и вывести список всех файлов
if safe_chdir(os.path.join(current_directory, 'PZ_11')):
    files = [f for f in os.listdir() if os.path.isfile(f)]
    print("Файлы в PZ_11:", files)
    os.chdir(current_directory)  # Вернуться в корень проекта

# Создать папку test и тестовую структуру внутри нее
test_dir = os.path.join(current_directory, 'test')
if not os.path.exists(test_dir):
    os.makedirs(os.path.join(test_dir, 'test1'))

# Переместить два файла из PZ_6 в папку test
pz6_files = [
    os.path.join(current_directory, 'PZ_6', 'PZ_6_1.py'),
    os.path.join(current_directory, 'PZ_6', 'PZ_6_2.py'),

]

for file in pz6_files:
    if os.path.isfile(file):
        copyfile(file, os.path.join(test_dir, os.path.basename(file)))
    else:
        print(f"Файл {file} не существует.")

test1_dir = os.path.join(current_directory, 'test/test1')

# Копировать файл из PZ_7 в папку test
pz7_files = [os.path.join(current_directory, 'PZ_7', 'PZ_7_1.py')]
for file in pz7_files:
    if os.path.isfile(file):
        copyfile(file, os.path.join(test1_dir, 'test.txt'))
    else:
        print(f"Файл {file} не существует.")

# Вывод информации о размере файлов в папке test
test_files_sizes = {f: os.path.getsize(os.path.join(test_dir, f)) for f in os.listdir(test_dir) if os.path.isfile(os.path.join(test_dir, f))}
print("Размер файлов в test:", test_files_sizes)

# Перейти обратно в PZ_11 и найти файл с самым коротким именем
if safe_chdir(os.path.join(current_directory, 'PZ_11')):
    files = [f for f in os.listdir() if os.path.isfile(f)]
    shortest_name_file = min(files, key=len)
    print("Файл с самым коротким именем:", os.path.basename(shortest_name_file))
    os.chdir(current_directory)  # Вернуться в корень проекта


# Перейти в папку reports и открыть PDF файл
reports_dir = os.path.join(current_directory, 'reports')  # Замените на вашу папку
if safe_chdir(reports_dir):
    pdf_files = [f for f in os.listdir(reports_dir) if f.endswith('.pdf')]
    if pdf_files:
        os.startfile(os.path.join(reports_dir, pdf_files[0]))  # Открыть первый найденный PDF файл
    else:
        print("Нет PDF файлов в папке reports.")
    os.chdir(current_directory)  # Вернуться в корень проекта

# Удалить файл test.txt
test_file = os.path.join(test1_dir, 'test.txt')
if os.path.isfile(test_file):
    os.remove(test_file)
    print("Файл test.txt удален.")
else:
    print(f"Файл {test_file} не существует.")
