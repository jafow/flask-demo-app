from datetime import datetime
import json

from celery import Celery
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.api import upload
from app.config import configure_app, celery_config


db_orm = SQLAlchemy()
migrate = Migrate()


def create_app(app_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if app_config is None:
        configure_app(app)

    db_orm.init_app(app)
    migrate.init_app(app, db_orm)

    app.register_blueprint(upload)

    @app.route("/ping")
    def ping():
        return json.dumps({"status": "ok", "ping": f"{datetime.utcnow()}"})

    return app


def create_celery(celery_env=None):
    _config = celery_config(celery_env)
    print("configggggggggggg class")
    print(_config)

    _celery = Celery(
        'taskq',
        backend=_config.CELERY_RESULT_BACKEND,
        broker=_config.CELERY_BROKER_URL
    )
    _celery.conf.update(_config)
    return _celery
