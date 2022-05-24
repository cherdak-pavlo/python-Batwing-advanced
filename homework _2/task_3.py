class StrMixin:
    def print_name(self):
        for key in self.__dict__:
            print(f'{key}: {self.__dict__[key]}')


class Profile(StrMixin):
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex


person = Profile("Alex", "Veritas", "+380666669999", "Lviv, kolomyiska 66/99", "alexveritas@gmail.com", "13.12.2001",
                 "20", "man")

person.print_name()

# OUTPUT

# address : Lviv, kolomyiska 66/99
# age : 20
# birthday : 13.12.2001
# email : alexveritas@gmail.com
# last_name : Veritas
# name : Alex
# phone_number : +380666669999
# sex : man
