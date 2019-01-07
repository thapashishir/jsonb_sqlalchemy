from jsonb_app import app,db
from  jsonb_app.models import Book

with app.app_context():
    db.reflect()
    db.drop_all()
    db.create_all()
           