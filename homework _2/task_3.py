class StrMixin:
    def print_name(self):
        for k, v in self.__dict__.items():
            print(f'{k}: {v}')


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

# name: Alex
# last_name: Veritas
# phone_number: +380666669999
# address: Lviv, kolomyiska 66/99
# email: alexveritas@gmail.com
# birthday: 13.12.2001
# age: 20
# sex: man
