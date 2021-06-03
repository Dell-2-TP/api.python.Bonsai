#Example model
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from model import db,ma
from sqlalchemy.sql.schema import ForeignKey
from model import education

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    # ed_id = db.Column(db.Integer, db.ForeignKey('education.id'))
    educations = db.relationship('Education', backref='employee')



    def __init__(self,name) -> None:
        self.name=name



#Temp Employee Schema

class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('id','name')