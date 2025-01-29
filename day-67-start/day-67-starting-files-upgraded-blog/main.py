from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_SERVE_LOCAL'] = False
app.config['CKEDITOR_PKG_TYPE'] = 'standard'

ckeditor = CKEditor(app)
# ckeditor.init_app(app)
Bootstrap5(app)
current_date = datetime.now()

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

class PostForm(FlaskForm):
    title = StringField(label="The blog post title", validators=[DataRequired()])
    subtitle = StringField(label="The subtitle", validators=[DataRequired()])
    author = StringField(label="The author's name", validators=[DataRequired()])
    img_url = URLField(label="A URL for the background image", validators=[DataRequired()])
    body = CKEditorField(label="The body (the main content) of the post", validators=[DataRequired()])
    submit = SubmitField(label="Submit post")
with app.app_context():
    db.create_all()

def to_dict(data):
    return {column.name: getattr(data, column.name) for column in data.__table__.columns}

def new_data(data):
    new_post = BlogPost(
        title=data.title.data,
        subtitle=data.subtitle.data,
        author=data.author.data,
        img_url=data.img_url.data,
        body=data.body.data,
        date=current_date.strftime("%B %d, %Y")
    )
    db.session.add(new_post)
    db.session.commit()
@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = BlogPost.query.all()
    result = [to_dict(item) for item in posts]
    print(result)
    return render_template("index.html", all_posts=result)

# TODO: Add a route so that you can click on individual posts.
@app.route('/show_post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    post = BlogPost.query.get(post_id)
    return render_template("post.html", post=post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        new_data(post_form)
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=post_form)
# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    post_form = PostForm(obj=post)
    if post_form.validate_on_submit():
        post.title = post_form.title.data
        post.subtitle = post_form.subtitle.data
        post.img_url = post_form.img_url.data
        post.author = post_form.author.data
        post.body = post_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=post_form, post=post)
# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = BlogPost.query.get(post_id)
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
