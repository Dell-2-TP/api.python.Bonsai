from flask import Flask
from service.job_service import JobService
class JobController(object):
    def __init__(self,app:Flask,service:JobService) -> None:
        self.app=app
        self.service=service
        self.add_routes(app)
    def add_routes(self,app:Flask):
        app.add_url_rule('/job',methods=['GET'],view_func=self.job)
        app.add_url_rule('/job',methods=['POST'],view_func=self.add_job)

    def job(self):
        return self.service.job()
    def add_job(self):
        return self.service.add_job()