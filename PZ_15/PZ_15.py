# Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для автоматизированного контроля затрат на производство продукции.
# БД должна содержать таблицу Расходы со следующей структурой записи: Дата, Код продукта, Наименование продукта, Расходы, Сумма.

import sqlite3

connect = sqlite3.connect('expences.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Expences (
    id integer PRIMARY KEY AUTOINCREMENT,
    ProductDate DATETIME,
    Code TEXT,
    ProductName TEXT,
    Expences TEXT,
    Amount REAL
)''')

cursor.executemany('''INSERT INTO Expences (ProductDate, Code, ProductName, Expences, Amount) VALUES(?, ?, ?, ?, ?)''', [
    ('2023-01-01', 'П01', 'Продукт 1', 'Сырье', 100.00),
    ('2023-01-02', 'П02', 'Product 2', 'Производство', 200.00),
    ('2023-01-03', 'П03', 'Product 3', 'Маркетинг', 300.00),
    ('2023-01-02', 'П04', 'Product 4', 'Логистика', 200.00),
    ('2023-01-02', 'П05', 'Product 5', 'Реклама', 250.00),
    ('2023-01-03', 'П06', 'Product 6', 'Консультации', 400.00),
    ('2023-01-02', 'П07', 'Product 7', 'Лес', 200.00),
    ('2023-01-02', 'П08', 'Product 8', 'Нефть', 600.00),
    ('2023-01-02', 'П09', 'Product 9', 'Налоги', 100.00),
    ('2023-01-02', 'П010', 'Product 10', 'Рабочие', 600.00),

])

connect.commit()

# Select
cursor.execute("SELECT * FROM expences WHERE id%2==00")
result = cursor.fetchall()
for item in result:
    print('1', item)
print()

cursor.execute("SELECT * FROM expences WHERE ProductDate=='2023-01-03'")
result = cursor.fetchall()
for item in result:
    print('2',item)
print()

cursor.execute("SELECT * FROM expences WHERE Amount>500")
result = cursor.fetchall()
for item in result:
    print('3', item)
print()

# Update
cursor.execute("UPDATE expences SET Amount=625 WHERE Amount>500 ")
cursor.execute("SELECT * FROM expences WHERE Amount>500 ")
result = cursor.fetchall()
for item in result:
    print('4', item)
print()

cursor.execute("UPDATE expences SET Code='П011' WHERE Code='П010' ")
cursor.execute("SELECT * FROM expences WHERE Code='П011' ")
result = cursor.fetchall()
for item in result:
    print('5', item)
print()

cursor.execute("UPDATE expences SET Amount=550 WHERE Expences='Нефть' ")
cursor.execute("SELECT * FROM expences WHERE Expences='Нефть' ")
result = cursor.fetchall()
for item in result:
    print('6', item)
print()

# Delete
cursor.execute("DELETE FROM expences WHERE id%2!=0 ")
cursor.execute("SELECT * FROM expences")
result = cursor.fetchall()
for item in result:
    print('7', item)
print()

cursor.execute("DELETE FROM expences WHERE ProductDate='2023-01-02' ")
cursor.execute("SELECT * FROM expences")
result = cursor.fetchall()
for item in result:
    print('8', item)

#Удалить все чтобы не повторялось
cursor.execute("DELETE FROM Expences")


connect.commit()

cursor.close()
connect.close()