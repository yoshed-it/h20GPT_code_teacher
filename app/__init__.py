from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    return app


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app
