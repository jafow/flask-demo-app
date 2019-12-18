""" Account Model """

from datetime import datetime

from sqlalchemy import Column, BigInteger, DateTime, String
from app.extensions import db_orm as orm


class Account(orm.Model):
    __tablename__ = "account"

    id = Column(BigInteger, primary_key=True)
    description = Column(String(length=128), nullable=True, default="No description")
    created_at = Column("created_at", DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column("updated_at", DateTime(timezone=True), default=datetime.utcnow)

    members = orm.relationship("Member")
