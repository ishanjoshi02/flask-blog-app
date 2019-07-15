from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask_login import LoginManager

import sys
import pymysql

from instance.config import get_database_string

from blog.main.controllers import main
from blog.posts.controllers import posts
from blog.users.controllers import users

from blog.users.data.models import User
from blog.posts.data.models import Post

app = Flask(__name__)
app.config.from_pyfile('../instance/config.py')

app.register_blueprint(main, url_prefix="/")
app.register_blueprint(posts, url_prefix="/post")
app.register_blueprint(users, url_prefix="/user")

# todo initialize session for User and Post

db_url = get_database_string("dev")

if sys.platform == "darwin":
    pymysql.install_as_MySQLdb()

engine = create_engine(db_url)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

User.init_session(session)
Post.init_session(session)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

@login_manager.user_loader
def load_user(id):
    if id:
        return session.query(User).get(int(id))
    else:
        return None
