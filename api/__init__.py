from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from api.config.config import config_by_name
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
jwt = None


def create_app(config_name):
    global jwt

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt = JWTManager(app)

    # 블루프린트
    from .domain.question.api import question_api
    app.register_blueprint(question_api.bp)

    # 필터
    from .common.filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    app.secret_key = app.config['SECRET_KEY']

    return app
