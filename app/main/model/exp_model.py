from model import db, ma

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    def __init__(self, description, start_date, end_date):
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

class ExperienceSchema(ma.Schema):
    class Meta:
        fields = ('id','description', 'start_date', 'end_date')