from flask_restful import Resource, marshal
from flask import request
from app.models import Municipio
from app import db
from app.schemas import municipio_field
import json


class Municipios(Resource):
    def post(self):
        data = json.loads(request.data)
        nome = data["nome"]
        id_estado = data["id_estado"]
        if Municipio.query.filter(Municipio.nome == nome,Municipio.id_estado == id_estado).one_or_none():
            return {"message":f"Município {nome} já está cadastrado"}
        else:
            municipio = Municipio(nome, id_estado)
            db.session.add(municipio)
            db.session.commit()
            return marshal(municipio, municipio_field, "municipio")
    

class ListaMunicipios(Resource):
    def get(self, id=None):
        municipios = Municipio.query.filter(Municipio.id_estado == id).all()
        print(municipios)
        if municipios != None:
            return marshal(municipios, municipio_field, "municipios")
        else:
            return {"message":"Id do estado não informado"}

    def put(self, id=None):
        data = json.loads(request.data)
        nome = data["nome"]
        municipio = Municipio.query.get(id)
        if not municipio:
            return {"message":"Municipio está tentando atualizar não existe"}
        
        municipio.nome = nome
        db.session.add(municipio)
        db.session.commit()
        return marshal(municipio, municipio_field, "municipio")

    def delete(self, id=None):
        municipio = Municipio.query.get(id)
        if not municipio:
            return {"message":"Municipio está tentando deletar não existe"}

        db.session.delete(municipio)
        db.session.commit()
        return marshal(municipio, municipio_field, "municipio")