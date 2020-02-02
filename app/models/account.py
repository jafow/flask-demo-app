""" account model """

from app.extensions import db_orm, NULL_ACCT_ID
from app.db.account import Account


class AccountModel(Account):
    """ account model methods """

    def __init__(self, app):
        super().__init__()
        self.app = app

    def create(self, accounts: list):
        """ making a REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEAAAALY long line """
        results = []
        with self.app.app_context():
            for account in accounts:
                if isinstance(account, dict):
                    acct_obj = Account(**account)
                else:
                    aid = {
                        "id": int(account) if account else NULL_ACCT_ID
                    }
                    acct_obj = Account(**aid)
                db_orm.session.merge(acct_obj)
                results.append(acct_obj)
            db_orm.session.commit()
        return results
