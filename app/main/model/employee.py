from os import name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from model import db, ma


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable = False)
    job = db.Column(db.String(100), nullable = False)

    def __init__(self,name,job) -> None:
        self.name=name
        self.job=job


class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('id','name','job')

