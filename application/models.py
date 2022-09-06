from application import db
from flask_login import LoginManager,UserMixin

class User():
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String,nullable=False)
    levelname = db.Column(db.String(16),unique=True,nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username