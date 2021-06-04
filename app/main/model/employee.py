#Example model
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from model import db,ma
from sqlalchemy.sql.schema import ForeignKey
from model.education import Education
from model.exp_model import Experience
from model.job import Job


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    job =  db.Column(db.String(100))
    # ed_id = db.Column(db.Integer, db.ForeignKey('education.id'))
    job = db.relationship("Job", uselist=False, backref="employee")
    educations = db.relationship('Education', backref='employee')
    experiences = db.relationship('Experience', backref='experience')



    def __init__(self,name,job) -> None:
        self.name=name,
        self.job=job



#Temp Employee Schema

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Employee
        
