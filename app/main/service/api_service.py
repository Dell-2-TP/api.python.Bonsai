from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

from model.example import Example, ExampleSchema
from model.education import Education, EducationSchema
class Service(object):
    def __init__(self,app:Flask,db:SQLAlchemy) -> None:
       self.app=app
       self.db=db
       self.example_schema=ExampleSchema()
       self.education_schema=EducationSchema()
       self.educations_schema=EducationSchema(many=True)

    def example(self):
        return 'example result'

    def add_example(self):
        example = Example(request.json['name'])
        self.db.session.add(example)
        self.db.session.commit()
        return self.example_schema.jsonify(example)

    def add_education(self):
        emp_id = request.json['emp_id']
        institution = request.json['institution']
        field = request.json['field']
        degree = request.json['degree']

        education = Education(emp_id, institution, field, degree)
        self.db.session.add(education)
        self.db.session.commit()
        return self.education_schema.jsonify(education)

    # get all educations
    def get_educations(self):
        all_educations = Education.query.all()
        result = self.educations_schema.dump(all_educations)
        return self.educations_schema.jsonify(result)

    # get single education
    def get_education_by_id(self, id):
        education = Education.query.get(id)
        return self.education_schema.jsonify(education)

    def update_education(self):
        pass