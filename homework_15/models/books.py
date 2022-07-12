from postgresdb import db


class Books(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(300), nullable=False)
    year = db.Column(db.Integer, nullable=False)

