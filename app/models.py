from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Articles(db.Model):
    __tablename__ = "Articles"
    id = db.Column('article_id', db.Integer, primary_key=True, autoincrement=True)
    title = db.Column('title', db.String(300))
    description = db.Column('description', db.String(1000))
    created_at = db.Column('created_at', db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column('updated_at', db.DateTime)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True)
    password = db.Column('password', db.String(10))
    registered_on = db.Column('registered_on', db.DateTime)


