from app import app
from app.model import Endereco
from flask import jsonify


@app.route('/<cepadd>')
def consulta(cepadd):
    res = Endereco.query.filter_by(cep=cepadd).first()
    if res:
        return jsonify([
            {"CEP": res.cep,
             "Complemento":res.complemento,
             "Logradouro": res.logradouro,
            "Bairro":res.bairro,
             "Cidade":res.cidade,
             "Estado":res.estado,
             "DDD": res.ddd,
             }
        ])
