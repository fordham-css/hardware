# ourapp/models.py
from . import db

class Engine(db.Model):
    # Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.String(128))
    item_status = db.Column(db.String(128))