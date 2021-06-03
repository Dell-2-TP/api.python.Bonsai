from sqlalchemy.sql.schema import ForeignKey
from model import db, ma

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, ForeignKey('employee.id'))
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    def __init__(self, employee_id, description, start_date, end_date):
        self.description = description
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date

class ExperienceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'employee_id', 'description', 'start_date', 'end_date')