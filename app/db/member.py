""" Member model """
from datetime import datetime

from sqlalchemy import Column, BigInteger, Sequence, DateTime, String, ForeignKey
from sqlalchemy.ormm import relationship

from app.database import orm


class Member(orm.Model):
    __tablename__ = "member"

    id = Column(BigInteger, Sequence("member_id_seq"), primary_key=True, index=True)
    mem_id = Column(BigInteger, nullable=False, index=True)
    fname = Column(String(length=128), nullable=True)
    lname = Column(String(length=128), nullable=True)
    phone = Column(String(length=128), nullable=False, index=True)
    acct_id = Column(BigInteger, ForeignKey("account.acct_id"), nullable=False, index=True)
    created_at = Column("created_at", DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column("updated_at", DateTime(timezone=True), default=datetime.utcnow)

    account = relationship('Account', backref="member")
