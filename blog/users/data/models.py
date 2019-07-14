from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from werkzeug.security import check_password_hash, generate_password_hash

from blog.posts.data.models import Post

import datetime

Base = declarative_base()


class User(Base):

    session = None

    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True, default=0)
    name = Column("name", String, nullable=False)
    username = Column("username", String, nullable=False)
    password = Column("password", String, nullable=False)
    created_on = Column(TIMESTAMP, default=datetime.datetime.now())

    is_authenticated = True
    is_active = True
    is_anonymous = False

    def __init__(self, firstname, lastname, username, password):

        self.name = f"{firstname} {lastname}"
        self.username = username
        self.password = generate_password_hash(password)

    def __repr__(self):

        return f"<User name: {self.name} username: {self.username}>"

    def get_id(self):
        return str(self.id).encode("utf-8").decode("utf-8")

    @classmethod
    def init_session(cls, session):
        cls.session = session

    # todo create check session decorator

    @classmethod
    def get(cls, id):
        if not cls.session:
            raise Exception("Session for UserClass not set."
                            "\nSet Class session using init_session static method of the class")
        # Todo check if user exists based on id. If not, raise exception
        return cls.session.query(cls).get(id)

    @classmethod
    def check_if_username_exists(cls, username):
        return cls.session.query(cls).filter(cls.username == username).count != 0

    @classmethod
    def get_session(cls):

        return cls.session

    def register_user(self):
        id= User.session.query(User).order_by(User.id.desc()).first().id + 1
        User.get_session().add(self)
        User.get_session().commit()
        if id == None:
            return 1
        return id

    def create(self):
        return self.register_user()

    def get_blogs(self):
        return Post.session.query(Post).filter(Post.author == self.id).filter(Post.deleted_on == None).all()


    @classmethod
    def auth(cls, username, password):
        # todo check if username exists
        query = cls.session.query(cls).filter(cls.username == username)
        for row in query:
            if check_password_hash(row.password, password):
                return [True, row]
        return False
