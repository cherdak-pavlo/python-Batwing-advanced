class StrMixin:
    def info_person(self):
        pass


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

person.info_person()