from app import db
import uuid
from datetime import datetime
from .estado_producto import Estado_producto

class Sucursal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    external_id = db.Column(db.String(60), default = str(uuid.uuid4()), nullable = False)
    nombre = db.Column(db.String(60), nullable = False)
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default = datetime.now)
    updated_at = db.Column(db.DateTime, default = datetime.now, onupdate=datetime.now)

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'nombre' : self.nombre,
            'latitud' : self.latitud,
            'longitud' : self.longitud
        }

