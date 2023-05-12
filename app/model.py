from app import app, db


class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(8), unique=True)
    logradouro = db.Column(db.String(120))
    complemento = db.Column(db.String(120))
    bairro = db.Column(db.String(120))
    cidade = db.Column(db.String(120))
    estado = db.Column(db.String(32))
    ddd = db.Column(db.String(2))


with app.app_context():
    db.create_all()

