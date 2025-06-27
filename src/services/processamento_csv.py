import pandas as pd
import os
CAMINHO_CSV= 'data/Ano-2025.csv'

def baixar_csv():
    if not os.path.exists(CAMINHO_CSV):
        raise FileNotFoundError(f'O arquivo {CAMINHO_CSV} não foi encontrado.')
    df = pd.read_csv(CAMINHO_CSV, sep=';', encoding='latin1', low_memory=False)
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