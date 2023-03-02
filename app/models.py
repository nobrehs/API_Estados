from app import db


class Estado(db.Model):
    __tablename__ = "estados"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    sigla = db.Column(db.String(2), nullable = False)

    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla

    def __repr__(self):
        return f"<Estado {self.nome}"
    

class Municipio(db.Model):
    __tablename__ = "municipios"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    id_estado = db.Column(db.Integer, nullable=False)

    def __init__(self, nome, id_estado):
        self.nome = nome
        self.id_estado = id_estado

    def __repr__(self):
        return f"<Município {self.nome}"