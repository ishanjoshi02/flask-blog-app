from flask import Blueprint, redirect, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__, template_folder="templates")

@main.route("/")
@login_required
def index():

    return render_template("index.html", name=current_user.name, blogs=current_user.get_blogs())

@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@main.route("/login")
def login():
    return redirect('/user/login')

@main.route("/register")
def register():
    return redirect("/user/register")

@main.route("/logout")
def logout():
    return redirect("/user/logout")