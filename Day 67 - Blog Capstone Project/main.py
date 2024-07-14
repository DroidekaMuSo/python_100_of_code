from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

from blogs_form import ADD_POST

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def to_dict(self):
        dictionary = {}

        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)

        return dictionary

    def get_all_posts(self):
        with app.app_context():
            result = db.session.execute(db.select(BlogPost).order_by(BlogPost.id)).scalars().all()

            return result

    def get_post_by_id(self, blog_id):
        with app.app_context():
            result = db.get_or_404(BlogPost, blog_id)

            return result

    def add_post(self, new_post):
        db.session.add(new_post)
        db.session.commit()


with app.app_context():
    db.create_all()

blog_manager = BlogPost()


@app.route(rule='/')
def get_all_posts():
    #Query the database for all the posts. Convert the data to a python list.
    all_blogs = blog_manager.get_all_posts()
    posts = [blog.to_dict() for blog in all_blogs]

    return render_template("index.html", all_posts=posts)


# Add a route so that you can click on individual posts.
@app.route(rule='/post/<int:post_id>')
def show_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    requested_post = blog_manager.get_post_by_id(post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route(rule="/new_post", methods=["POST", "GET"])
def create_post():
    add_post_form = ADD_POST()

    if add_post_form.validate_on_submit():
        new_post = BlogPost(
            title=add_post_form.title.data,
            subtitle=add_post_form.subtitle.data,
            date=date.today().strftime("%B %d, %Y"),
            body=add_post_form.body.data,
            author=add_post_form.author.data,
            img_url=add_post_form.img_url.data,
        )
        blog_manager.add_post(new_post)
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=add_post_form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["POST", "GET"])
def edit_post(post_id):
    post = blog_manager.get_post_by_id(post_id)
    add_post_form = ADD_POST(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body
    )

    if add_post_form.validate_on_submit():
        post.title = add_post_form.title.data
        post.subtitle = add_post_form.subtitle.data
        post.img_url = add_post_form.img_url.data
        post.author = add_post_form.author.data
        post.body = add_post_form.body.data

        db.session.commit()
        return redirect(url_for('show_post', post_id=post.id))

    return render_template(template_name_or_list="make-post.html", post=post, form=add_post_form)


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = blog_manager.get_post_by_id(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
