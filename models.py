from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #why this is needed and write SQLAlchemy.Model but why it is not possible

# retaltion between Contact class and db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(250),nullable=False)