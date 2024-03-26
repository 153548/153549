class Person:
    def __init__(self, name, rare, country):
        self.name = name
        self.rare = rare
        self.country = country
        print(f'Создан человек с именем {name}')

    def __del__(self):
        print(f'Удален человек с именем {self.name}')


sanya = Person('Sanya', 0.00001, 'HIPHOP')

