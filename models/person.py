from app import db

class Persona(db.Model):
    #__tablename__ = "rol"
    
    id = db.Column(db.Integer, primary_key = True)
    external_id = db.Column(db.String(60))
    name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    age = db.Column(db.Integer)