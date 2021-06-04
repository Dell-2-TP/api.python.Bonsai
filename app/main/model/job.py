#Example model
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.sql.schema import ForeignKey
from model import db, ma

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    title = db.Column(db.String(100), unique=True)
    salary = db.Column(db.Float)

    def __init__(self,employee_id, title, salary) -> None:
        self.employee_id=employee_id
        self.title = title
        self.salary = salary

#Job Schema
class JobSchema(ma.Schema):
    class Meta:
        fields = ('id','employee_id','title', 'salary')