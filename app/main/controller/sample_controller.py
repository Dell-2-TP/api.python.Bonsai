from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from service.api_service import Service
class SampleController(object):
    def __init__(self,app:Flask,db:SQLAlchemy,service:Service) -> None:
        self.app=app
        self.db=db
        self.service=service
        self.add_routes(app)
    def add_routes(self,app:Flask):
        app.add_url_rule('/example',methods=['GET'],view_func=self.example)
        app.add_url_rule('/example',methods=['POST'],view_func=self.add_example)
    def example(self):
        return self.service.example()
    def add_example(self):
        return self.service.add_example()