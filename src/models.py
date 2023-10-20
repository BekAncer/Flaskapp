from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


metadata = MetaData()
db = SQLAlchemy()


class Sneaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    imgsrc = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Article %r>' % self.id
