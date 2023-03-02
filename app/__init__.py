from flask_restful import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate



db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    api = Api(app)
    db.init_app(app)
    migrate.init_app(app,db)

    from app.resources.estados import Estados
    api.add_resource(Estados, "/estados")
    from app.resources.municipios import Municipios
    api.add_resource(Municipios, "/municipios")
    from app.resources.municipios import ListaMunicipios
    api.add_resource(ListaMunicipios, "/municipios/<int:id>")

    return(app)