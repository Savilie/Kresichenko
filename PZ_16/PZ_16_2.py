# Создайте класс "Животное", который содержит информацию о виде и возрасте животного.
# Создайте классы "Собака" и "Кошка", которые наследуются от класса "Животное" и содержат информацию о породе.


class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age


class Dog(Animal):
    def __init__(self, age, breed):
        super().__init__("Собака", age)  # Передаем "Собака" как species
        self.breed = breed

    def __str__(self):
        return f"{self.species} {self.age} {self.breed}"

class Cat(Animal):
    def __init__(self, age, breed):
        super().__init__("Кошка", age)  # Передаем "Кошка" как species
        self.breed = breed

    def __str__(self):
        return f"{self.species} {self.age} {self.breed}"


dog1 = Dog(5, 'Лабрадор')

print(dog1.__str__())

cat1 = Cat(4, 'Сфинкс')

print(cat1.__str__())
