import os
from datetime import datetime

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# что здесь конфиги забыли?
load_dotenv()
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASS = os.environ.get("POSTGRES_PASSWORD")
DB_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

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
