from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, Flask, request
from model.job import Job, JobSchema
class JobService(object):
    def __init__(self,db:SQLAlchemy, app: Flask) -> None:
       self.app = app
       self.db=db
       self.job_schema=JobSchema(many = True)
       self.one_job_schema = JobSchema()

    def job(self):
        all_jobs = Job.query.all()
        return self.job_schema.jsonify(all_jobs)

    def one_job(self, id):
        one_job = Job.query.get(id)
        return self.one_job_schema.jsonify(one_job)

    def add_job(self):
        job = Job(request.json['employee_id'],request.json['title'], request.json['salary'])
        self.db.session.add(job)
        self.db.session.commit()
        return self.one_job_schema.jsonify(job)

    def update_job(self):
        job = Job.query.get(request.json['id'])

        title = request.json['title']
        salary = request.json['salary']

        job.title = title
        job.salary = salary

        self.db.session.commit()

        return self.one_job_schema.jsonify(job)

    def delete_job(self, id):
        job = Job.query.get(id)
        self.db.session.delete(job)
        self.db.session.commit()
        return self.one_job_schema.jsonify(job)
