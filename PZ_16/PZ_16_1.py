# Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
# Добавьте методы для вычисления процентных начислений и снятия денег.

import pickle

class Bank():
    def __init__(self, amount, interest_rate):
        self.amount = amount
        self.interest_rate = interest_rate

    def calculate_interest(self):
        self.amount += (self.amount * self.interest_rate) / 100
        return self.amount

    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount -= amount
        else:
            print('Недостаточно средств на балансе')

# Использование функций
bank = Bank(100, 5)
rate = bank.calculate_interest()
print("Прибыль от процентов", rate)
bank.withdraw(20)
print('Сумма счета после снятия денег', bank.amount)


def save_def(bank_list):
    with open('bank_data.pkl', 'wb') as f:
        pickle.dump(bank_list, f)

def load_def():
    try:
        with open('bank_data.pkl', 'rb') as f:
            bank_list = pickle.load(f)
        return bank_list
    except FileNotFoundError:
        return None

# Пример использования
bank1 = Bank(1000, 5)
bank2 = Bank(2000, 10)
bank3 = Bank(3000, 15)

bank_list = [bank1, bank2, bank3]

# Сохранение экземпляров класса в файл
save_def(bank_list)

# Загрузка экземпляров класса из файла
loaded_bank_list = load_def()

# Проверка загруженных экземпляров класса
for bank in loaded_bank_list:
    print(bank.amount, bank.interest_rate)