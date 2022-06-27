class UserDB:
    users = [{"name": "test", "email": "test@test.com", "password": "passhash"}]

    def get_all(self):
        return self.users

    def retrieve_by_email(self, email):
        for user in self.users:
            if user["email"] == email:
                return user
        return "No user with this email"

    def add(self, name, email, password_hash):
        user = {
            "name": name,
            "email": email,
            "password": password_hash
        }
        for retrieve_user in self.users:
            if email in retrieve_user["email"]:
                return 'User already exists'
        else:
            self.users.append(user)
            return user

    def update_by_email(self, email, name, password):
        for user in self.users:
            if user["email"] == email:
                user["name"] = name
                user["password"] = password
                return user
        return "No user with this email"

    def delete_by_email(self, email):
        self.users = [user for user in self.users if user["email"] != email]


class BookDB:
    books = [{"id": "1", "author": "test", "name": "Test Name 1"}]

    def get_all(self):
        return self.books

    def retrieve_by_id(self, id):
        for book in self.books:
            if book["id"] == id:
                return book
        return "No book with this id"

    def add(self, id, author, name):
        book = {
            "id": id,
            "author": author,
            "name": name
        }
        for retrieve_book in self.books:
            if id in retrieve_book["id"]:
                return 'Book already exists'
        else:
            self.books.append(book)
            return book

    def update_by_id(self, id, author, name):
        for book in self.books:
            if book["id"] == id:
                book["name"] = name
                book["author"] = author
                return book
        return "No book with this id"

    def delete_by_id(self, id):
        self.books = [book for book in self.books if book["id"] != id]
