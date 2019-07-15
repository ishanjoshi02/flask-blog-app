from flask import Blueprint, render_template, redirect, request,flash
from flask_login import current_user

from .data.models import Post
from .data.forms import BlogForm
from blog.users.data.models import User

import json

posts = Blueprint('posts', __name__, template_folder="templates")

@posts.route("/")
def index():
    return "blogs"

@posts.route("/new", methods=["GET", "POST"])
def create_post():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_post = Post(title, content, author=current_user.id)
        id =new_post.create()
        return redirect(f"/post/{id}")

    return render_template("post_blog.html", form=form)

@posts.route("/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    post = Post.get(id)
    form = BlogForm()
    if current_user.id == post.author:

        if request.method == "GET":

            form.title.data = post.title
            form.content.data = post.content
            return render_template("edit_blog.html", form=form, id=id)

        elif form.validate_on_submit():

            title = form.title.data
            content = form.content.data
            post.update(title, content)
            flash("Post updated successfully")
            return redirect(f"/post/{id}")

@posts.route("/<int:id>", methods=["GET", "DELETE"])
def blog(id):

    if request.method == "GET":
        return get_post(id)
    elif request.method == "DELETE":
        post = Post.get(id)
        if post.author == current_user.id:
            post.delete()
            flash("Blog deleted successfully")
            return json.dumps(True)



def get_post(id):
    post = Post.get(id)
    author = User.get(post.author)
    return render_template("view_blog.html",
                           title=post.title,
                           content=post.content,
                           blog_id=post.id,
                           editable=(current_user.id is post.author),
                           author=author.name,author_id=author.id,
                           )

@posts.route("/<int:start>/<int:end>")
def get_posts(start, end):
    posts = Post.get_all()

    ret_val = []
    if len(posts) < end:
        end = len(posts)
    for i in range(start, end, 1):
        blog = posts[i]
        temp = dict(blog)
        temp['author'] = User.get(int(temp['author'])).name
        ret_val.append(temp)
    return json.dumps(ret_val)
