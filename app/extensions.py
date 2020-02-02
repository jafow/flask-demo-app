""" flask extensions """
import logging

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

db_orm = SQLAlchemy(session_options={"expire_on_commit": False})
migrate = Migrate()
ma = Marshmallow()

NULL_ACCT_ID = 4199
