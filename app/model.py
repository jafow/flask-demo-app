# """ member model """

# from app.extensions import db_orm
# from app.db.account import Member


# class MemberModel(Member):
#     """ member model methods """

#     def __init__(self, app):
#         super().__init__()
#         self.app = app

#     def create(self, members: list):
#         results = []
#         with self.app.app_context():
#             for member in members:
#                 member_obj = Member(**member)
#                 db_orm.session.add(member_obj)
#                 results.append(member_obj)
#             db_orm.session.commit()
#         return results
