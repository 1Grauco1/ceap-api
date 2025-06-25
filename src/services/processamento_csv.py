import pandas as pd
import requests
from io import BytesIO
from zipfile import ZipFile

URL_CSV= "https://www.camara.leg.br/cotas/Ano-2025.csv.zip"

def baixar_csv():
    response = requests.get(URL_CSV, timeout=30)
    response.raise_for_status()
    
    with ZipFile(BytesIO(response.content)) as zip_file:
        csv_filename = [f for f in zip_file.namelist() if f.endswith('.csv')][0]
        with zip_file.open(csv_filename) as csv_file:
            df = pd.read_csv(
                csv_file, 
                sep=';', 
                encoding='latin1',
                dtype={'cpf': str},  
                parse_dates=['dataEmissao'],  
                dayfirst=True 
            )
    return df

def filtrar_e_converter_dados(dp):
    if dp.empty:
        return []
    
    dp= dp[dp['sgUF'].notna()][[
        'txNomeParlamentar', 'cpf', 'sgPartido', 'sgUF',
        'dataEmissao', 'txtFornecedor', 'vlrLiquido', 'urlDocumento'
    ]].copy()
    
    despesas= []
    for _, row in dp.iterrows():
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