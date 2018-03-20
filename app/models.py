from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Articles(db.Model):
    __tablename__ = "Articles"
    id = db.Column('article_id', db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column('author_id', db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column('title', db.String(300))
    description = db.Column('description', db.String(1000))
    created_at = db.Column('created_at', db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column('updated_at', db.DateTime)

    def is_updated(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S') != self.updated_at.strftime('%Y-%m-%d %H:%M:%S')


class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True)
    password = db.Column('password', db.String(10))
    registered_on = db.Column('registered_on', db.DateTime, default=db.func.current_timestamp())

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % (self.username)


