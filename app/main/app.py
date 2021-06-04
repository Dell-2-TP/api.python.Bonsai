from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from service.api_service import Service
from controller.sample_controller import SampleController
from model import db
from flask_swagger_ui import get_swaggerui_blueprint
#init application context
app = Flask(__name__)

#sqlalchemy database config, dialect://user:pass@url:port/dbname
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password123@localhost:5432/Bonsai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Bonsai"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###
#init service, routes. might refactor to init multiple with a single initialization
service = Service(app,db)
sample_controller = SampleController(app,service)


if(__name__=='__main__'):
    db.init_app(app)
    app.run(debug=True)