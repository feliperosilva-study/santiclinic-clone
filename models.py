from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Clientes (db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    telemovel = db.Column(db.Integer, nullable=False)
    consulta = db.Column(db.String(200))
    duvida = db.Column(db.String(500))