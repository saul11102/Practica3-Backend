from flask import Blueprint, jsonify, make_response, request
from flask_expects_json import expects_json
from routes.schemas.schema_sucursal import save_sucursal
from control.sucursal_control import SucursalControl
from control.utils.errors import Errors
from control.Authenticate import token_required

api_sucursal = Blueprint('api_sucursal_sucursal', __name__)

sucursalC = SucursalControl()


@api_sucursal.route('/sucursal')
#@token_required
def home():
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "datos" : ([i.serialize for i in sucursalC.listar()])}), 
        200
    )

@api_sucursal.route('/sucursal/guardar'   , methods = ["POST"])
#@token_required
@expects_json(save_sucursal)
def guardar_sucursal():
    data = request.json 
    id = sucursalC.guardarSucursal(data = data)
    if(id >= 0):
        return make_response(
                jsonify({"msg" : "OK", "code" : 200, "datos" : {"tag" : "datos guardados"}}), 
                200
        )
    else:
        return make_response(
                jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Errors.error[str(id)]}}), 
                400
    )



