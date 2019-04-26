import os
from datetime import datetime
from flask import Blueprint, render_template, url_for, flash, redirect, request, abort, current_app
from flask_login import current_user, login_required
from woo import db
from woo.posts.forms import PostForm
from woo.models import Post
from woo.posts.utils import save_picture

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
        else:
            picture_file = None
        post = Post(title=form.title.data, content=form.content.data, author=current_user, image_file=picture_file)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created", "success")
        return redirect(url_for("main.home"))
    return render_template("create_post.html", title="New Post",
                           form=form, legend="Update Post")


@posts.route("/post/<int:post_id>")
def post(post_id):
    post1 = Post.query.get_or_404(post_id)
    return render_template("post.html", title=post1.title, post=post1)


@posts.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        try:
            picture_path = os.path.join(current_app.root_path, "static/post_pics", post.image_file)
            os.remove(picture_path)
        except:
            pass
        post.title = form.title.data
        post.content = form.content.data
        if form.picture.data:
            post.image_file = save_picture(form.picture.data)
        else:
            post.image_file = None
        post.date_posted = datetime.utcnow()
        db.session.commit()
        flash("Your post has been updated!", "success")
        return redirect(url_for("posts.post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template("create_post.html", title="Update Post",
                           form=form, legend="Update Post")


@posts.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    try:
        picture_path = os.path.join(current_app.root_path, "static/post_pics", post.image_file)
        os.remove(picture_path)
    except:
        pass
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", "success")
    return redirect(url_for("main.home"))

