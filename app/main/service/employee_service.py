   
from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from model.employee import Employee, EmployeeSchema


class EmployeeService(object):
    def __init__(self,app:Flask,db:SQLAlchemy) -> None:
       self.app=app
       self.db=db
       self.employee_schema = EmployeeSchema()
       self.employee_schema_many = EmployeeSchema(many=True)

    def add_employee(self):
        name = request.json['name']

        new_employee = Employee(name)

        self.db.session.add(new_employee)
        self.db.session.commit()
        result = self.employee_schema.jsonify(new_employee)

        return result

    def get_employees(self):
        all_employees = Employee.query.all()
        result = jsonify(self.employee_schema_many.dump(all_employees))
        return result

    def get_employee(self, id):
        employee = Employee.query.get(id)
        result = self.employee_schema.jsonify(employee)
        return result

    def update_employee(self, id):
        employee = Employee.query.get(id)
        
        name = request.json['name']

        employee.name = name
    

        self.db.session.commit()

        result = self.employee_schema.jsonify(employee)

        return result
    #todo: fix cascading delete
    def delete_employee(self, id):
        employee = Employee.query.get(id)
        
        self.db.session.delete(employee)
        self.db.session.commit()

        result = self.employee_schema.jsonify(employee)

        return result