"""create user and post tables

Revision ID: 2b38ad510d2c
Revises: 
Create Date: 2019-07-14 12:16:03.553869

"""
from alembic import op
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP


# revision identifiers, used by Alembic.
revision = '2b38ad510d2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        Column('id', Integer, primary_key=True,
               autoincrement=True, default=0),
        Column('name', String(255), nullable=False),
        Column('password', String(1000), nullable=False),
        Column('username', String(256), nullable=False)
    )

    op.create_table(
        'posts',
        Column('id', Integer, primary_key=True,
               autoincrement=True, default=0),
        Column('title', String(255), nullable=False),
        Column('content', String(10000), nullable=False),
        Column('author', Integer, ForeignKey('users.id'), nullable=False),
        Column('created_on', TIMESTAMP),
        Column('edited_on', TIMESTAMP, nullable=True),
        Column('deleted_on', TIMESTAMP, nullable=True)
    )



def downgrade():
    op.drop_table('posts')
    op.drop_table('users')
