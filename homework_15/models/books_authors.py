from postgresdb import db


class BooksAuthors(db.Model):
    __tablename__ = 'books_authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    books = db.relationship("Books")
    authors = db.relationship("Authors")
