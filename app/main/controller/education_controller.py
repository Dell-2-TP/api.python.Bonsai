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

    def update_education(self, id):
        return self.service.update_education(id)

    def delete_education(self, id):
        return self.service.delete_education(id)
    