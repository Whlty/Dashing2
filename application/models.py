from application import db
from flask_login import LoginManager,UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16),unique=True,nullable=False)
    levels = db.Column(db.String(16),unique=True,nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username