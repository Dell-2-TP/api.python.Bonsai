#Example model
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from model import db,ma, employee
from sqlalchemy.sql.schema import ForeignKey

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    institution = db.Column(db.String(100))
    field = db.Column(db.String(100))
    degree = db.Column(db.String(100))



    def __init__(self,emp_id,institution,field,degree) -> None:
        self.employee_id=emp_id
        self.institution=institution
        self.field=field
        self.degree=degree



#Education Schema

class EducationSchema(ma.Schema):
    class Meta:
        fields = ('id','emp_id', 'institution','field', 'degree')