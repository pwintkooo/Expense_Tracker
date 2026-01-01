from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    userName = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Expense(db.Model):
    expense_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id", name="fk_expense_user_id"))
    created_at = db.Column(db.DateTime, default=datetime.now)