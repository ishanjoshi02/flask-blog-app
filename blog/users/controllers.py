from flask import Blueprint, render_template, redirect
from flask_login import login_user, current_user, logout_user

from .data.forms import LoginForm, RegisterForm

from .data.models import User

users = Blueprint('users', __name__, template_folder="templates")


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        auth = User.auth(username, password)

        if auth[0]:
            login_user(
                auth[1],
                remember=True
            )
            return redirect("/")
        else:
            print("Invalid login")

    return render_template("login.html", form=form)


@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect("/")
    form = RegisterForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        password = form.password.data

        new_user = User(firstname, lastname, username, password)
        new_user.create()

        login_user(new_user, remember=True)

        return redirect("/")

    return render_template('register.html', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect('/login')

@users.route("/<int:id>")
def get_user(id):
    user = User.get(id)
    name = user.name
    username = user.username
    blogs = user.get_blogs()
    return render_template("view_user.html", name=name, username=username, blogs=blogs)
