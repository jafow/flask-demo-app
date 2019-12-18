""" conftest """
from datetime import datetime
import pytest
from flask import current_app
from sqlalchemy_utils import create_database, database_exists

from app import create_app
from app.extensions import db_orm, NULL_ACCT_ID
from app.db.member import Member, Account


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.testing = True
    app.config.from_object("app.config.TestingConfiguration")
    return app


@pytest.fixture(scope="session")
def client(app):
    with app.test_client() as client:
        context = app.app_context()
        context.push()
        yield client
        context.pop()


@pytest.fixture(scope="session")
def db(app, request):
    with app.app_context():
        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(current_app.config["SQLALCHEMY_DATABASE_URI"])

        db_orm.drop_all()
        db_orm.create_all()

        def teardown():
            db_orm.drop_all()

        request.addfinalizer(teardown)
        yield db_orm


@pytest.fixture
def account_fixture(app, request, db):
    """ create accountt object test fixture """
    acct = {"id": NULL_ACCT_ID, "description": "NULL testing account"}
    acct = Account(**acct)
    db.session.add(acct)
    db.session.commit()

    def cleanup():
        db.session.delete(acct)

    request.addfinalizer(cleanup)

    yield acct


@pytest.fixture
def member_fixture(app, request, db, account_fixture):
    """ returns a function to create member object test fixture """

    def _member_fixture(member_dict: dict):
        defaults = {
            "mem_id": 145667,
            "fname": "test",
            "lname": "test last",
            "phone": "555-555-1234",
            "acct_id": NULL_ACCT_ID,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
        }
        merged = {**defaults, **member_dict}
        member = Member(**merged)
        db.session.add(member)
        db.session.commit()

        def cleanup():
            db.session.delete(member)

        request.addfinalizer(cleanup)
        return member
    yield _member_fixture
