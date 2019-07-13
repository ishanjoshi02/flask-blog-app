from flask import Flask
from blog.main.controllers import main
from blog.posts.controllers import posts
from blog.users.controllers import users


app = Flask(__name__)

app.register_blueprint(main, url_prefix="/")
app.register_blueprint(posts, url_prefix="/posts")
app.register_blueprint(users, url_prefix="/user")
