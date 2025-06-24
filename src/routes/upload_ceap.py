from flask import Blueprint, jsonify
from services.processamento_csv import baixar_csv, filtrar_e_converter_dados
from controllers.deputado_controller import salvar_despesas

upload_bp= Blueprint('upload_ceap', __name__)
@upload_bp.route('/upload-ceap', methods=['POST'])

def upload_ceap():
    try:
        df= baixar_csv()
        despesas= filtrar_e_converter_dados(df)
        salvar_despesas(despesas)
        return jsonify({"Mensagem": "Dados importados", "total": len(despesas)})
    except Exception as e:
        return jsonify({"error": str(e)})
