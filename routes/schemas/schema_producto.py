save_producto = {
    'type' : 'object',
    'propierties' : {
        'nombre': {'type' : 'string'},
        'precio': {'type' : 'float'},
        'codigo_lote' : {'type': 'string'},
        'nombre_sucursal' : {'type: string'},
    },
    'required' : ['nombre','precio','codigo_lote', 'nombre_sucursal']
}