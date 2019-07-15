
# About the Project

The goal of this project was to create a Flask based Web App, that allows users to register and sign in.
Signed in users can post blogs, edit blogs and delete blogs(Only their own blogs).

Apart from this, the site features a dashboard, which loads all the available Blogs on the Web App.

Unauthenticated users also get to read posts.


# Tech Stack

1. Flask (Python based light-weight framework)
2. SQLAlchemy
3. Jinja Templating Framework
4. MySQL Database

# Installation Instructions

Make sure you have `alembic` installed.

1. `git clone https://github.com/ishanjoshi02/flask-blog-app.git`
2. `pip install -r requirements`
3. `alembic upgrade head`
4. `python run.py`

# Installation Instructions for developers

You do need to follow the above instructions before doing this.

`pip install -r developer_requirements.txt`


