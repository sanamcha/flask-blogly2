"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

DEFAULT_IMAGE ="http://www.pixelstalk.net/wp-content/uploads/2016/12/Color-Splash-Wallpaper-Full-HD.jpg"



class User(db.Model):
    """User Table."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False, unique=True)
    last_name = db.Column(db.String, nullable=True)

    image_url = db.Column(db.Text, nullable=False, default = DEFAULT_IMAGE)
    posts = db.relationship('Post', backref='user', cascade='all, delete-orphan')

    @property
    def full_name(self):
        """Return full name"""
        return f"{self.first_name} {self.last_name} "

class Post(db.Model):
    """Post table"""
    __tablename__ ="posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.now )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # user=db.relationship('User', backref='posts')


    # def __repr__(self):
    #     p =self
    #     return f"<Post id ={p.id} title={p.title} content={p.content} created_at={p.created_at} user_id={p.user_id}> "


def connect_db(app):
    db.app = app
    db.init_app(app)