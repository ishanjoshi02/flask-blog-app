"""add created_on column to user table

Revision ID: 6d81c5587d37
Revises: 2b38ad510d2c
Create Date: 2019-07-14 12:32:33.566340

"""
from alembic import op
from sqlalchemy import Column, TIMESTAMP


# revision identifiers, used by Alembic.
revision = '6d81c5587d37'
down_revision = '2b38ad510d2c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "users",
        Column(
            "created_on", TIMESTAMP
        )
    )


def downgrade():
    pass
