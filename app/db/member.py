from datetime import datetime

from sqlalchemy import Column, Integer, Sequence, DateTime, String, ForeignKey

from app.extensions import db_orm as orm
from app.db.account import Account


class Member(orm.Model):
    __tablename__ = "member"

    id = Column(Integer, Sequence("member_id_seq"), primary_key=True, index=True)
    mem_id = Column(Integer, nullable=True, index=True)
    fname = Column(String(length=128), nullable=True)
    lname = Column(String(length=128), nullable=True)
    phone = Column(String(length=128), nullable=False, index=True)
    acct_id = Column(ForeignKey("account.id"), nullable=False, index=True)
    created_at = Column("created_at", DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column("updated_at", DateTime(timezone=True), default=datetime.utcnow)

    account = orm.relationship("Account")

    def __repr__(self):
        return "<Member(id=%s, mem_id=%s, fname=%s, lname=%s, acct_id=%s)>" % (
            self.id,
            self.mem_id,
            self.fname,
            self.lname,
            self.acct_id,
        )
