from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from service.job_service import JobService
from controller.job_controller import JobController
from service.exp_service import ExperienceService
from controller.exp_controller import ExperienceController
from service.education_service import EducationService
from controller.education_controller import EducationController
from model import db
from controller.employee_controller import EmployeeController
from service.employee_service import EmployeeService

#init application context
app = Flask(__name__)

#sqlalchemy database config, dialect://user:pass@url:port/dbname
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password123@localhost:5432/Bonsai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



#init service, routes. might refactor to init multiple with a single initialization
job_service = JobService(db, app)
job_controller = JobController(app,job_service)
edu_service = EducationService(app,db)
education_controller = EducationController(app,edu_service)

employeeservice = EmployeeService(app,db)
employee_controller = EmployeeController(app,employeeservice)

exp_service = ExperienceService(app, db)
exp_controller = ExperienceController(app, exp_service)

if(__name__=='__main__'):
    db.init_app(app)
    app.run(debug=True)