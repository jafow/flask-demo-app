"""create accounts table

Revision ID: 44656de915c9
Revises:
Create Date: 2019-12-16 03:09:00.677834

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "44656de915c9"
down_revision = None
branch_labels = None
depends_on = None

table = "account"
seq = f"{table}_id_seq"


def upgrade():
    # op.execute(f"CREATE SEQUENCE {seq}")
    op.create_table(
        table,
        sa.Column("id", sa.BigInteger, primary_key=True),
        # sa.Column("acct_id", sa.BigInteger, index=True, nullable=False),
        sa.Column(
            "description",
            sa.String(length=128),
            nullable=True,
            default="No description",
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), default=datetime.utcnow),
        sa.Column("updated_at", sa.DateTime(timezone=True), default=datetime.utcnow),
    )


def downgrade():
    # op.execute(f"DROP SEQUENCE {seq}")
    op.drop_table(table)
