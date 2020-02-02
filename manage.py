""" manage """

import csv
from datetime import datetime

from app import create_app
from app.extensions import db_orm, NULL_ACCT_ID
from app.models.member import MemberModel
from app.models.account import AccountModel

app = create_app()
cli = app.cli


@cli.command()
def hello():
    print("hello")


@cli.command()
def loadmembers():
    """ load members from csv """
    db_orm.drop_all()
    db_orm.create_all()

    # create null account type
    AccountModel(app).create([{"id": NULL_ACCT_ID, "description": "NULL ACCOUNT"}])

    with open("data/member_data.csv") as f:
        reader = csv.DictReader(f)
        lines = [
            {
                # "id": line["id"],
                "fname": line["first_name"],
                "lname": line["last_name"],
                "phone": line["phone_number"],
                # set members without account id to a "null account" id
                "mem_id": line.get("client_member_id", NULL_ACCT_ID),
                "acct_id": line.get("account_id"),
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow(),
            }
            for line in reader
        ]

        # setup the accounts ref data
        ac = {line["acct_id"] for line in lines}
        AccountModel(app).create(ac)

        # create members
        res = MemberModel(app).create(lines)
        # db_orm.session.commit()
        print(f"created {len(res)}")


if __name__ == "__main__":
    cli()
