""" flask app configuration """
import os


ENV_CONFIG_PATHS = {
    "default": "app.config.DefaultConfiguration",
    "test": "app.config.TestingConfiguration"
}


class DefaultConfiguration(object):
    DEBUG = True
    REGION = "us-east-1"
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    CELERY_BROKER_URL = 'redis://redis:6379/0'
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:pg_pass@db:5432/main"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfiguration(DefaultConfiguration):
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:pg_pass@db:5432/test"


def configure_app(app, flask_env=None):
    if not flask_env:
        app_config_name = os.getenv('FLASK_ENV', 'default')

    app.config.from_object(ENV_CONFIG_PATHS[app_config_name])


def celery_config(celery_env=None):
    if celery_env and celery_env.upper() == "TEST":
        return TestingConfiguration()
    return DefaultConfiguration
