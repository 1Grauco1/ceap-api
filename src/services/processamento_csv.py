import pandas as pd
import requests
from io import StringIO

URL_CSV= "https://www.camara.leg.br/cotas/Ano-2025.csv.zip"

def baixar_csv():
    try:
        response= requests.get(URL_CSV, timeout=30)
        response.raise_for_status()  

        csv_data= StringIO(response.content.decode('latin1'))
        return pd.read_csv(csv_data, sep=';', encoding='latin1')
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro ao baixar CSV da Câmara: {str(e)}")

def filtrar_e_converter_dados(df):
    if df.empty:
        return []
    
    df= df[df['sgUF'].notna()][[
        'txNomeParlamentar', 'cpf', 'sgPartido', 'sgUF',
        'dataEmissao', 'txtFornecedor', 'vlrLiquido', 'urlDocumento'
    ]].copy()
    
    despesas= []
    for _, row in df.iterrows():
        despesas.append({
            'nome': row['txNomeParlamentar'],
            'cpf': row['cpf'],
            'partido': row['sgPartido'],
            'uf': row['sgUF'],
            'data_emissao': row['dataEmissao'],
            'fornecedor': row['txtFornecedor'],
            'valor': float(row['vlrLiquido']), 
            'url_documento': row['urlDocumento']
        })
    
    return despesas