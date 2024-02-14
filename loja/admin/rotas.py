#Importando as bibliotecas para o caminho

from flask import render_template, session, request, url_for

from loja import app, db

#criando o app para rotas(pasando a rota entre os parenteses,'/' = esta na raiz)
@app.route('/')

#Pagina principal
def home():
    return "Olá mundo"

@app.route('/registrar')

#Pagina principal
def registrar():
    return render_template('admin/registrar.html', title="Registrar user")