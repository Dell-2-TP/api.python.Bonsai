from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from model.exp_model import Experience, ExperienceSchema

class ExperienceService(object):
    def __init__(self, app:Flask, db:SQLAlchemy) -> None:
        self.app = app
        self.db = db
        self.exp_schema = ExperienceSchema()
        self.exps_schema = ExperienceSchema(many=True)

    # Creating new experience
    def add_experience(self):
        description = request.json['description']
        employee_id = request.json['employee_id']
        start_date = request.json['start_date']
        end_date = request.json['end_date']

        new_experience = Experience(employee_id, description, start_date, end_date)

        self.db.session.add(new_experience)
        self.db.session.commit()

        return self.exp_schema.jsonify(new_experience)

    # Retreiving all experiences
    def get_experiences(self):
        all_experiences = Experience.query.all()

        return jsonify(self.exps_schema.dump(all_experiences))

    # Retreiving single experience
    def get_experience(self, id):
        experience = Experience.query.get(id)

        return self.exp_schema.jsonify(experience)

    # Updating single experience
    def update_experience(self, id):
        experience = Experience.query.get(id)
        
        employee_id = request.json['employee_id']
        description = request.json['description']
        start_date = request.json['start_date']
        end_date = request.json['end_date']

        experience.employee_id = employee_id
        experience.description = description
        experience.start_date = start_date
        experience.end_date = end_date

        self.db.session.commit()

        return self.exp_schema.jsonify(experience)

    # Deleting single experience
    def delete_experience(self, id):
        experience = Experience.query.get(id)
        
        self.db.session.delete(experience)

        self.db.session.commit()

        return self.exp_schema.jsonify(experience)