from datetime import datetime
import json

from celery import Celery
from flask import Flask

from app.api import api, upload
from app.config import configure_app, celery_config

from app.extensions import db_orm, migrate, ma


def create_app(app_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if app_config is None:
        configure_app(app)

    db_orm.init_app(app)
    migrate.init_app(app, db_orm)
    ma.init_app(app)

    app.register_blueprint(upload)
    app.register_blueprint(api)

    @app.route("/ping")
    def ping():
        return json.dumps({"status": "ok", "ping": f"{datetime.utcnow()}"})

    return app


def create_celery(celery_env=None):
    _config = celery_config(celery_env)

    _celery = Celery("taskq", backend=_config.CELERY_RESULT_BACKEND, broker=_config.CELERY_BROKER_URL)
    _celery.conf.update(_config)
    return _celery
