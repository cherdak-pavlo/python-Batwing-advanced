# Task #1

class Animal:
    """Dog has 3 methods (eat, sleep, drink) """

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} eats every day')

    def sleep(self):
        print(f'{self.name} likes to sleep')

    def drink(self):
        print(f'{self.name} drinks water every few hours')

    def print_info(self):
        print(f'Animal name is {self.name}\n')


class Cat(Animal):
    """Cat has 1 unique method (print how many years it lives)"""

    def __init__(self, name, age):
        super().__init__(name)
        self.age = int(age)

    def how_many_years(self):
        print(f'{self.name} lives {self.age} y/o')


class Bird(Animal):
    """Bird has method (printing his color feathers)"""

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color.lower()

    def animal_color(self):
        print(f'{self.name} has {self.color} feathers')


class Horse(Animal):
    """Horse has method (say igo-go)"""

    def __init__(self, name):
        super().__init__(name)

    def language_horse(self):
        print(f'{self.name} says: "Igo-go"')


class Mole(Animal):
    """Mole has method (printing that usually sleeps underground)"""

    def __init__(self, name):
        super().__init__(name)

    def sleep_underground(self):
        print(f'{self.name} usually sleeps underground')


class Bear(Animal):
    """Bear has 1 unique method (print what it likes to eat)"""

    def __init__(self, name, favorite_food='honey'):
        super().__init__(name)
        self.food = favorite_food.lower()

    def like_eat(self):
        print(f'{self.name} likes to eat {self.food}')


cat_mike = Cat('Mike', age=4)
cat_mike.how_many_years()
print(issubclass(Cat, Animal))

bird_lorry = Bird('Lorry', color='Red')
bird_lorry.animal_color()
print(issubclass(Bird, Animal))

horse_lucky = Horse('Lucky')
horse_lucky.language_horse()
print(issubclass(Horse, Animal))

mole_gera = Mole('Gera')
mole_gera.sleep_underground()
print(issubclass(Mole, Animal))

bear_ivan = Bear('Ivan', favorite_food='Fish')
bear_ivan.like_eat()
print(issubclass(Bear, Animal))


# Task #1a


class Human:
    def __init__(self, surname, age, weight, height):
        self.surname = surname
        self.age = age
        self.weight = weight
        self.height = height

    def print_info(self):
        print(f'My Surname is {self.surname}\n'
              f'I have {self.age} y\o\n'
              f'My weight is {self.weight} kg\n'
              f'My height is {self.height}')


class Centaur(Human, Animal):
    def __init__(self, name, surname, age, weight, height, color_tail):
        Human.__init__(self, surname, age, weight, height)
        Animal.__init__(self, name)
        self.color_tail = color_tail

    def info_about_centaur(self):
        print(f'Name_centaur: {self.name}\n'
              f'Centaur surname: {self.surname}\n'
              f'Age_centaur: {self.age}\n'
              f'Weight_centaur: {self.weight}\n'
              f'Height_centaur: {self.height}\n'
              f'Color his tail: {self.color_tail.lower()}')


obj = Centaur('Petro', 'Pushpa', age=3001, weight=250, height=195, color_tail='Orange')
print('-' * 75)
obj.print_info()
print('-' * 75)
obj.info_about_centaur()
