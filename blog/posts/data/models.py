from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import  declarative_base

Base = declarative_base()


class Post(Base):

    __tablename__ = "posts"

    id = Column("id", Integer, primary_key=True, autoincrement=True, default=0)
    title = Column("title", String, default="")
    content = Column("content", String, default="")
    author_id = Column("author", Integer, ForeignKey("user.id"))
    created_on = Column(TIMESTAMP)
    deleted_on = Column(TIMESTAMP)
    edited_on = Column(TIMESTAMP)

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __iter__(self):
        yield "id", self.id
        yield "title", self.title
        yield "content", self.content
        yield "author", self.author

    def __repr__(self):
        return "<BlogModel title: {} AuthorId: {} >".format(self.name, self.author)
