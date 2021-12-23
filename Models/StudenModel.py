from db import db

class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    second_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    birthday = db.Column(db.Date, nullable=False)
    course = db.Column(db.Integer, default=1)
