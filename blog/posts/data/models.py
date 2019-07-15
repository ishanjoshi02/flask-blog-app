from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

import datetime

Base = declarative_base()


class Post(Base):

    session = None

    __tablename__ = "posts"

    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=True, default=0)
    title = Column("title", String, default="")
    content = Column("content", String, default="")
    author = Column("author", Integer)
    created_on = Column(TIMESTAMP)
    deleted_on = Column(TIMESTAMP)
    edited_on = Column(TIMESTAMP)

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_on = datetime.datetime.now()

    def __iter__(self):
        yield "id", self.id
        yield "title", self.title
        yield "content", self.content
        yield "author", self.author

    def __repr__(self):
        return "<BlogModel title: {} AuthorId: {} >".format(self.title, self.author)

    @classmethod
    def init_session(cls, session):
        cls.session = session

    # todo create session exists decorator

    def create(self):
        try:
            id= Post.session.query(Post).order_by(Post.id.desc()).first().id + 1
        except:
            id = 1
        Post.session.add(self)
        Post.session.commit()
        return id


    @classmethod
    def get(cls, id):
        if not cls.session:
            raise Exception("Session for UserClass not set."
                            "\nSet Class session using init_session static method of the class")
            # Todo check if user exists based on id. If not, raise exception
        if id:
            if type(id) == String:
                id = int(id)
            return cls.session.query(cls).get(id)

        return cls.get_all()

    @classmethod
    def get_all(cls):
        return cls.session.query(cls).filter(cls.deleted_on == None).all()

    def update(self, title, content):
        # todo check if blog exists
        Post.session.query(Post).filter(self.id == Post.id).update({
            "title": title,
            "content": content,
            "edited_on": datetime.datetime.now()
        })
        Post.session.commit()

    def delete(self):
        # todo check if blog exists.
        Post.session.query(Post).filter(Post.id == self.id).update({
            "deleted_on": datetime.datetime.now()
        })
        Post.session.commit()