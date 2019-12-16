"""create member table

Revision ID: 8755b1a380ea
Revises: 44656de915c9
Create Date: 2019-12-16 03:08:44.970497

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8755b1a380ea'
down_revision = "44656de915c9"
branch_labels = None
depends_on = None


table = "member"
seq = f"{table}_id_seq"


def upgrade():
    op.execute(f"CREATE SEQUENCE {seq}")
    op.create_table(
        table,
        sa.Column("id", sa.BigInteger, autoincrement=True, primary_key=True),
        sa.Column("mem_id", sa.BigInteger, index=True, nullable=False),
        sa.Column("fname", sa.String(length=128), nullable=True),
        sa.Column("lname", sa.String(length=128), nullable=True),
        sa.Column("phone", sa.String(length=128), nullable=False, index=True),
        sa.Column("acct_id", sa.BigInteger, sa.ForeignKey("account.acct_id"), nullable=False, index=True),
        sa.Column("created_at", sa.DateTime(timezone=True), default=datetime.utcnow),
        sa.Column("updated_at", sa.DateTime(timezone=True), default=datetime.utcnow),
    )


def downgrade():
    op.execute(f"DROP SEQUENCE {seq}")
    op.drop_table(table)
