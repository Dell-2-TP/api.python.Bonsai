from flask import Flask
from service.api_service import Service
class EducationController(object):
    def __init__(self,app:Flask,service:Service) -> None:
        self.app=app
        self.service=service
        self.add_routes(app)

    def add_routes(self,app:Flask):
        # add
        app.add_url_rule('/education',methods=['POST'],view_func=self.add_education)
        # get all
        app.add_url_rule('/education',methods=['GET'],view_func=self.get_educations)
        # get single
        app.add_url_rule('/education/<id>',methods=['GET'],view_func=self.get_education_by_id)
        # get all by employee id
        app.add_url_rule('/education/empid/<emp_id>',methods=['GET'], view_func=self.get_educations_by_emp_id)
        # get all by institution
        app.add_url_rule('/education/institution/<institution>', methods=['GET'], view_func=self.get_by_institution)
        # get all by degree
        app.add_url_rule('/education/degree/<degree>', methods=['GET'], view_func=self.get_by_degree)
        # get all by field
        app.add_url_rule('/education/field/<field>', methods=['GET'], view_func=self.get_by_field)
        # update education
        app.add_url_rule('/education/<id>', methods=["PUT"],view_func=self.update_education)
        # delete education
        app.add_url_rule('/education/<id>', methods=["DELETE"],view_func=self.delete_education)


        

    def add_education(self):
        return self.service.add_education()

    def get_educations(self):
        return self.service.get_educations()

    def get_education_by_id(self, id):
        return self.service.get_education_by_id(id)

    def get_educations_by_emp_id(self, emp_id):
        return self.service.get_educations_by_emp_id(emp_id)

    def get_by_institution(self, institution):
        return self.service.get_by_institution(institution)

    def get_by_degree(self, degree):
        return self.service.get_by_degree(degree)

    def get_by_field(self, field):
        return self.service.get_by_field(field)

    def update_education(self, id):
        return self.service.update_education(id)

    def delete_education(self, id):
        return self.service.delete_education(id)
    