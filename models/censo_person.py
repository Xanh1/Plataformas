from app import db
import uuid

class Censo_Persona(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    external_id = db.Column(db.String(60), default = str(uuid.uuid4()))
    date = db.Column(db.Date)