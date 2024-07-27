from models.sucursal import Sucursal
import uuid
from app import db
from datetime import datetime, timedelta
from flask import current_app  

class SucursalControl:
    Sucursal = Sucursal()
    def listar(self):
        return Sucursal.query.all()
    
    def guardarSucursal(self, data):
        if data:  
            sucursal_aux = Sucursal()
            sucursal_aux.external_id = uuid.uuid4()
            sucursal_aux.nombre = data['nombre']
            sucursal_aux.latitud = data ['latitud']
            sucursal_aux.longitud = data ['longitud']
            db.session.add(sucursal_aux)
            db.session.commit()
            
            return sucursal_aux.id   
        else:
            return -2
        