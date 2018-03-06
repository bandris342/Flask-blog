from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(300))
    description = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

