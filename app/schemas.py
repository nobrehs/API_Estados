from flask_restful import fields

estado_field = {
    "id": fields.Integer,
    "nome": fields.String,
    "sigla": fields.String
}

municipio_field = {
    "id":fields.Integer,
    "nome":fields.String,
    "id_estado":fields.Integer
}