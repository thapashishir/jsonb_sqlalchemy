from sqlalchemy.dialects.postgresql import JSONB
from jsonb_app import db

class Book (db.Model):
    __tablename__ = "books"

    id_ = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSONB)

    def __init__(self,data):
        self.data = data