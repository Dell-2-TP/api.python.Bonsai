from flask import Flask
from service.exp_service import ExperienceService

class ExperienceController(object):
    def __init__(self, app:Flask, service:ExperienceService) -> None:
        self.app = app
        self.service = service
        self.add_routes(app)

    def add_routes(self, app:Flask):
        app.add_url_rule('/experience', methods=['POST'], view_func=self.add_experience)
        app.add_url_rule('/experience', methods=['GET'], view_func=self.get_experiences)
        app.add_url_rule('/experience/<id>', methods=['GET'], view_func=self.get_experience)
        app.add_url_rule('/experience/<id>', methods=['PUT'], view_func=self.update_experience)
        app.add_url_rule('/experience/<id>', methods=['DELETE'], view_func=self.delete_experience)

    def add_experience(self):
        return self.service.add_experience()
    
    def get_experiences(self):
        return self.service.get_experiences()
        
    def get_experience(self, id):
        return self.service.get_experience(id)

    def update_experience(self, id):
        return self.service.update_experience(id)

    def delete_experience(self, id):
        return self.service.delete_experience(id)