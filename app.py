from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados_login.sqlite3'
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))
    cpf = db.Column(db.String(100))

    def __init__(self, nome, email, senha, cpf):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/index', methods=["GET", "POST"])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        cpf = request.form.get('cpf')

        if not nome or not email or not senha or not cpf:
            flash("Preencha todos os campos do formulário", "error")
        else:
            try:
                dados_login = Menu(nome, email, senha, cpf)
                db.session.add(dados_login)
                db.session.commit()
                flash("Cadastro realizado com sucesso!", "success")
                return redirect(url_for('principal'))
            except Exception as e:
                flash("Erro ao salvar os dados", "error")
                print("Erro:", e)
    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=os.getenv('FLASK_DEBUG', 'True') == 'True')
