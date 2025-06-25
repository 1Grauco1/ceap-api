from flask import Blueprint, request, jsonify
from controllers.deputado_controller import (
    list_deputados_uf,
    list_despesas_dp,
    calc_total_despesas
)

deputado_bp= Blueprint('deputado', __name__)

@deputado_bp.route('/deputado')
def get_deputados():
    uf= request.args.get('uf')
    deputados= list_deputados_uf(uf)
    return jsonify(deputados)

@deputado_bp.route('/deputado/<int:deputado_id>/despesas')
def get_despesas_dp(deputado_id):
    despesas= list_despesas_dp(deputado_id)
    return jsonify(despesas)

@deputado_bp.route('/total-depesas')
def get_total_despesas():
    total= calc_total_despesas()
    return jsonify(total)