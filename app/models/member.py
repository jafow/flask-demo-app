""" member model """

import logging

from app.extensions import db_orm
from app.db.member import Member

logger = logging.getLogger(__name__)


NULL_ACCT_ID = 4199


class MemberModel(Member):
    """ member model methods """
    def __init__(self, app):
        super().__init__()
        self.app = app

    def base_query(self, session):
        return session.query(Member)

    def only_new_members(self, members: list) -> bool:
        """ check a list of member dicts for existing and filter only new """
        existing = {m.mem_id for m in self.get("mem_id", [m["mem_id"] for m in members])}
        return [m for m in members if m["mem_id"] not in existing]

    def create(self, members: list):
        with self.app.app_context():
            instances = []
            new_members = self.only_new_members(members)
            for member in new_members:
                if not member.get('acct_id', None):
                    member["acct_id"] = NULL_ACCT_ID
                logger.debug(f"create member: {member}")
                member_obj = Member(**member)
                instances.append(member_obj)
                db_orm.session.add(member_obj)
            db_orm.session.commit()
        return instances

    def get(self, param, vals: list) -> list:
        """ get members """
        assert param, "should have parameter to get members by"

        query = self.base_query(db_orm.session)
        logger.debug(f"get member with param: {param} on vals {vals}")
        return query.filter(getattr(Member, param).in_(vals)).all()
