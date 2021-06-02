from flask import Flask
from service.api_service import Service
class JobController(object):
    def __init__(self,app:Flask,service:Service) -> None:
        self.app=app
        self.service=service
        self.add_routes(app)
    def add_routes(self,app:Flask):
        app.add_url_rule('/job',methods=['GET'],view_func=self.job)
        app.add_url_rule('/job',methods=['POST'],view_func=self.add_job)
        app.add_url_rule('/job/<id>', methods = ['GET'], view_func = self.get_one_job)
        app.add_url_rule('/job', methods = ['PUT'], view_func = self.update_one_job)
        app.add_url_rule('/job/<id>', methods=['DELETE'], view_func=self.delete_one_job)

    def job(self):
        result = self.service.job()
        return result

    def get_one_job(self, id):
        result = self.service.one_job(id)
        return result

    def add_job(self):
        return self.service.add_job()

    def update_one_job(self):
        return self.service.update_job()

    def delete_one_job(self, id):
        return self.service.delete_job(id)