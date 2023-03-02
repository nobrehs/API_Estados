from flask_restful import Resource, marshal
from flask import request
from app.models import Estado
from app import db
from app.schemas import estado_field
import json


class Estados(Resource):
    def get(self):
        estados = Estado.query.all()
        return marshal(estados, estado_field, "estados")

    def post(self):
        data = json.loads(request.data)
        nome = data["nome"]
        sigla = data["sigla"]
        if Estado.query.filter(Estado.nome == nome):
            return {"message":f"Estado {nome} já está cadastrado"}
        else:
            estado = Estado(nome, sigla)
            db.session.add(estado)
            db.session.commit()
            return marshal(estado, estado_field, "estados")

    def put(self):
        pass

    def delete(self):
        pass