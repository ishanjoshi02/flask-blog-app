from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True, default=0)
    name = Column("name", String, nullable=False)
    username = Column("username", String, nullable=False)
    password = Column("password", String, nullable=False)
    created_on = Column(TIMESTAMP, default=datetime.datetime.now())

    def __init__(self, firstname, lastname, username, password):

        self.name = f"{firstname} {lastname}"
        self.username = username
        self.password = password

    def __repr__(self):

        return f"<User name: {self.name} username: {self.username}>"