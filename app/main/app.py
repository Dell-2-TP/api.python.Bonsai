from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from service.api_service import Service
from controller.sample_controller import SampleController
from model import db

#init application context
app = Flask(__name__)

#sqlalchemy database config, dialect://user:pass@url:port/dbname
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password123@localhost:5432/Bonsai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



#init service, routes. might refactor to init multiple with a single initialization
service = Service(app,db)
sample_controller = SampleController(app,db,service)

if(__name__=='__main__'):
    db.init_app(app)
    app.run(debug=True)