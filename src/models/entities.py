from datetime import date
from config.database import db

class Deputado(db.Model):
    __tablename__= 'deputados'

    id= db.Column(db.Integer, primary_key= True)
    nome= db.Column(db.String(150), nullable= False)
    uf= db.Column(db.String(2), nullable= False)
    cpf= db.Column(db.String(20), unique= True)
    partido= db.Column(db.String(20))
    despesas= db.relationship('Dispesa', backref= 'deputado', lazy= True)

class Despesa(db.Model):
    __tablename__= 'despesas'

    id= db.Column(db.Integer, primary_key= True)
    dataEmissao= db.Column(db.Date)
    fornecedor= db.Column(db.String(150))
    valorLiquido= db.Column(db.Float)
    urlDocumento= db.Column(db.String(300))
    deputado_id= db.Column(db.Integer, db.ForeignKey('deputados.id', nullable= False))