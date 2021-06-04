from flask import Flask
from service.employee_service import EmployeeService

class EmployeeController(object):
    def __init__(self,app:Flask,service:EmployeeService) -> None:
        self.app = app
        self.service = service
        self.add_routes(app)

    def add_routes(self, app:Flask):
        app.add_url_rule('/employee', methods=['POST'], view_func=self.add_employee)
        app.add_url_rule('/employee', methods=['GET'], view_func=self.get_employees)
        app.add_url_rule('/employee/<id>', methods=['GET'], view_func=self.get_employee)
        app.add_url_rule('/employee/<id>', methods=['PUT'], view_func=self.update_employee)
        app.add_url_rule('/employee/<id>', methods=['DELETE'], view_func=self.delete_employee)

    def add_employee(self):
        return self.service.add_employee()
    
    def get_employees(self):
        return self.service.get_employees()
        
    def get_employee(self, id):
        return self.service.get_employee(id)

    def update_employee(self, id):
        return self.service.update_employee(id)

    def delete_employee(self, id):
        return self.service.delete_employee(id)