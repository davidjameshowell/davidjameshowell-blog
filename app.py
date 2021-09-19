from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import mistune
import time

app = Flask(__name__)
POSTS_PER_PAGE = 5

@app.template_filter('markdown')
def reverse_filter(s):
    if type(s) == str:
        markdown_post = mistune.html(s)
    else:
        markdown_post = mistune.html(s.decode('utf_8'))
    return markdown_post

@app.template_filter('epoch_to_date')
def epoch_to_time(created_date):
    pattern = '%m/%d/%Y'
    return time.strftime(pattern, time.localtime(created_date))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_db/blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    subtitle = db.Column(db.String(), nullable=False)
    slug = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.Integer(), nullable=False)
    content_hash = db.Column(db.String(), nullable=False)

class About(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(), nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(), nullable=False)

@app.route("/", defaults={'page': 1})
@app.route("/<int:page>")
def list_posts(page):
    if page is None:
        page = 0
    posts = Post.query.order_by(Post.created_on.desc()).paginate(page, POSTS_PER_PAGE, False)

    return render_template('list_posts.html', posts=posts)

@app.route("/post/<slug>")
def get_post(slug):
    post = Post.query.filter_by(slug=slug).first()
    return render_template('post.html', post=post, slug=slug)

@app.route("/about-me")
def about_me():
    about = About.query.filter_by(id=1).first()
    return render_template('about.html', about=about)

@app.route("/contact-me")
def contact_me():
    contact = Contact.query.filter_by(id=1).first()
    return render_template('contact.html', contact=contact)
