from flask import Flask, send_from_directory
from app_estoque.modelo import RepositorioProdutos, RepositorioOperacoes
from app_estoque.visao import plug_views

app = Flask(__name__, static_folder='static', static_url_path='/ui')

@app.route("/")
def root():
    return send_from_directory(app.static_folder, 'index.html')

repProdutos = RepositorioProdutos()
repOperacoes = RepositorioOperacoes(repProdutos)    
plug_views(app, repProdutos, repOperacoes)





