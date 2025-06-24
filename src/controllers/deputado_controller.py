from models.entities import Deputado, Despesa
from config.database import db
from datetime import datetime

def salvar_despesas(lista_despesas):
    try:
        for d in lista_despesas:
            #busca deputado
            deputado= Deputado.query.filter_by(cpf=d['cpf']).first() if d['cpf'] else None
            if not deputado:
                deputado= Deputado.query.filter_by(nome=d['nome'], uf=d['uf']).first()
            
            #novo deputado se não existir
            if not deputado:
                deputado= Deputado(
                    nome=d['nome'],
                    cpf=d['cpf'],
                    partido=d['partido'],
                    uf=d['uf']
                )
                db.session.add(deputado)
                db.session.commit()  
            
            #nova despesa
            nova_despesa= Despesa(
                dataEmissao=converter_data(d['data_emissao']),
                fornecedor=d['fornecedor'],
                valorLiquido=d['valor'],
                urlDocumento=d['url_documento'],
                deputado_id=deputado.id
            )
            db.session.add(nova_despesa)
        
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise e

def converter_data(data_str):
    try:
        return datetime.strptime(data_str, '%d/%m/%Y').date() if data_str else None
    except ValueError:
        return None