from app import db

class Rol(db.Model):
    #__tablename__ = "rol"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(200))
    status = db.Column(db.Boolean, default = True)
    external_id = db.Column(db.String(60))