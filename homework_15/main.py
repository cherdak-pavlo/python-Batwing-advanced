import http
from flask import Flask
from config import Config
from postgresdb import db
from api.books_api import books_router
from api.authors_api import authors_router
from api.books_authors import books_authors

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(books_router)
app.register_blueprint(authors_router)
app.register_blueprint(books_authors)
db.init_app(app)


@app.errorhandler(404)
def handle_404(e):
    return 'Sorry, this resource does not exist', http.HTTPStatus.NOT_FOUND


if __name__ == "__main__":
    app.run(host='0.0.0.0')
