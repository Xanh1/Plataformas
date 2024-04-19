from app import db


class Censo(db.Model):
	
    id = db.Column(db.Integer, primary_key = True)
    external_id = db.Column(db.String(60))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    description = db.Column(db.String(200))

