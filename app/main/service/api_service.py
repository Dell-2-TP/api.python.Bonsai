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

    # get single education by id
    def get_education_by_id(self, id):
        education = Education.query.get(id)
        return self.education_schema.jsonify(education)

    # get all educations matching employee_id
    def get_educations_by_emp_id(self, emp_id_int):
        all_educations = Education.query.filter(Education.emp_id==emp_id_int).all()
        result = self.educations_schema.dump(all_educations)
        return self.educations_schema.jsonify(result)

    # get educations by institution
    def get_by_institution(self, institution_string):
        all_educations = Education.query.filter(Education.institution==institution_string).all()
        result = self.education_schema.dump(all_educations)
        return self.education_schema.jsonify(result)


    # get educations by degree
    def get_by_degree(self, degree_str):
        all_educations = Education.query.filter(Education.degree==degree_str).all()
        result = self.education_schema.dump(all_educations)
        return self.education_schema.jsonify(result)

    # get educations by field
    def get_by_field(self, field):
        all_educations = Education.query.filter(Education.field==field).all()
        result = self.education_schema.dump(all_educations)
        return self.education_schema.jsonify(result)

    # update education by id
    def update_education(self, id):
        education = Education.query.get(id)

        emp_id = request.json['emp_id']
        institution = request.json['institution']
        field = request.json['field']
        degree = request.json['degree']

        education.emp_id = emp_id
        education.institution = institution
        education.field = field
        education.degree = degree

        self.db.session.commit()

        return self.education_schema.jsonify(education)


    def delete_education(self, id):
        education = Education.query.get(id)

        self.db.session.delete(education)
        self.db.session.commit()

        return self.education_schema.jsonify(education)
