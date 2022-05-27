from abc import abstractmethod, ABC
import random


class Person(ABC):
    def __init__(self, name, age, availability_of_money=True, having_own_home=False):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.having_own_home = having_own_home
        self.balance = 15000 if availability_of_money else 0

    def provide_info_person(self):
        print(f'\nName: {self.name}\n'
              f'Age: {self.age} years old.\n'
              f'Availability of money: {self.availability_of_money}\n'
              f'Having own home: {self.having_own_home}\n')

    @abstractmethod
    def make_money(self):
        raise NotImplementedError('This method is not implemented')

    @abstractmethod
    def buy_house(self, number_of_house):
        raise NotImplementedError('This method is not implemented')


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, houses, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def provide_info_houses(self):
        for house in self.houses:
            print(f'{house.house_name}: Area of house - {house.area} sq.m and it cost - {house.cost}$')

    def give_discount(self):
        print(f'I can give you {self.discount}% discount if you do not have your own home\n'
              f'Or {self.discount / 2}% discount if you have your own home')

    def apply_discount(self):
        for house in self.houses:
            if self.name.having_own_home:
                house.cost -= int(((self.discount / 2) / 100) * house.cost)
            else:
                house.cost -= int((self.discount / 100) * house.cost)
            print(f'For {house.house_name} discount activated! New price: {house.cost}$')

    def steal_money(self):
        if random.randrange(10) == 0:
            self.name.balance = 0
            print('Ooh... The realtor stole all your money')
        else:
            print('The realtor tried to steal the money, but he did not succeed')


class House:
    def __init__(self, area, cost, house_name):
        self.area = area
        self.cost = cost
        self.house_name = house_name

    def house_is_sold(self):
        self.house_name += '[SOLD OUT]'


class Human(Person):
    def __init__(self, name, age, availability_of_money, having_own_home):
        super().__init__(name, age, availability_of_money, having_own_home)

    def make_money(self):
        self.balance += 5000
        print(f"{self.name}'s balance now: {self.balance}")

    def buy_house(self, number_of_house):
        if '[SOLD OUT]' in number_of_house.house_name:
            print('This house has already been bought by someone. Choose another house')
        elif self.balance >= number_of_house.cost:
            self.balance -= number_of_house.cost
            print(f'Congratulations! you bought a new house for {number_of_house.cost}$. Features of your new home:\n'
                  f'- Area: {number_of_house.area} sq.m\n'
                  f'- Cost: {number_of_house.cost}$\n'
                  f'- Now your balance is {self.balance}$')
            self.having_own_home = True if self.having_own_home is False else None
            number_of_house.house_is_sold()
        else:
            print(f"Unfortunately, you can't buy this house because your balance is {self.balance}$ "
                  f"and the house costs {number_of_house.cost}$.")


home_13 = House(40, 13000, '#13')
home_89 = House(50, 17000, '#89')
john = Human('John', 21, True, False)
leo = Human('Leo', 29, True, False)
mike = Realtor(john, [home_13, home_89], discount=12)

mike.provide_info_houses()
mike.steal_money()
mike.give_discount()
mike.apply_discount()
john.buy_house(home_89)
mike.provide_info_houses()
leo.buy_house(home_13)
mike.provide_info_houses()
john.provide_info_person()
leo.provide_info_person()
