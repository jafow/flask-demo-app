""" Account Model """

from datetime import datetime

from sqlalchemy import Column, BigInteger, Sequence, DateTime, String

from app.database import orm


class Account(orm.Model):
    __tablename__ = "account"

    id = Column(BigInteger, Sequence("account_id_seq"), primary_key=True)
    acct_id = Column(BigInteger, index=True, nullable=False)
    description = Column(String(length=128), nullable=True, default="No description")
    created_at = Column("created_at", DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column("updated_at", DateTime(timezone=True), default=datetime.utcnow)
