from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

from model.example import Example, ExampleSchema
class Service(object):
    def __init__(self,app:Flask,db:SQLAlchemy) -> None:
       self.app=app
       self.db=db
       self.example_schema=ExampleSchema()
    def example(self):
        return 'example result'
    def add_example(self):
        example = Example(request.json['name'])
        self.db.session.add(example)
        self.db.session.commit()
        return self.example_schema.jsonify(example)