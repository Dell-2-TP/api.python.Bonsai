#Example model
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from model import db, ma

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    salary = db.Column(db.Float)

    def __init__(self, title, salary) -> None:
        self.title = title
        self.salary = salary

#Job Schema
class JobSchema(ma.Schema):
    class Meta:
        fields = ('id','title', 'salary')