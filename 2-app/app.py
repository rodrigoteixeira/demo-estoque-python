# coding=UTF-8
#!flask/bin/python
from flask import Flask, jsonify, request, abort, url_for, send_from_directory
from produtos import RepositorioProdutos, ElementoInexistente, ElementoInvalido
from operacoes import RepositorioOperacoes
import os


HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_400_BAD_REQUEST = 400
HTTP_404_NOT_FOUND  = 404

app = Flask(__name__, static_folder='static', static_url_path='/ui')
repProdutos = RepositorioProdutos()

@app.route("/")
def hello():
    return send_from_directory(app.static_folder, 'index.html')
    
    
@app.route('/app/produtos', methods=['GET'])
def list_Produtos():
    produtos = repProdutos.listar()
    return jsonify({'produtos': produtos})    
    
@app.route('/app/produtos', methods=['POST'])
def create_prod():
    try:
        if not request.json['id']:
            print( 'adicionar' )
            produto = repProdutos.adicionar(request.json)
        else:
            print( 'atualizar' )
            produto = repProdutos.atualizar(request.json)
            
        return jsonify({'resultado': produto}), HTTP_201_CREATED
    except ElementoInvalido:
       abort(HTTP_400_BAD_REQUEST)


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))