from flask import Flask

from auth.api import auth_router
from core.database import db
from config import Config
from event.api import event_router
from user.api import user_router

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(auth_router)
app.register_blueprint(user_router)
app.register_blueprint(event_router)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
