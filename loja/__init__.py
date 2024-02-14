#Importando as bibliotecas que utilizarei 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Iniciando o banco de dados
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhaloja.db'
db = SQLAlchemy(app)


#Chamando a rota 
from loja.admin import rotas