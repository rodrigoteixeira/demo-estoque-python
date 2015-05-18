# coding=UTF-8
#!flask/bin/python
from flask import Flask, jsonify, request, abort, url_for, send_from_directory
from flask.views import MethodView
from produtos import RepositorioProdutos, ElementoInexistente, ElementoInvalido
from operacoes import RepositorioOperacoes
import os

HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_400_BAD_REQUEST = 400
HTTP_404_NOT_FOUND  = 404

repProdutos = RepositorioProdutos()
repOperacoes = RepositorioOperacoes(repProdutos)

app = Flask(__name__, static_folder='static', static_url_path='/ui')
    

@app.route("/")
def root():
    return send_from_directory(app.static_folder, 'index.html')

class APIBasica (MethodView):
    def __init__(self, repositorio):
        self.repositorio = repositorio
        
    def get(self, elem_id):
        if elem_id is None:
            elementos = self.repositorio.listar()
            return jsonify({'resultado': elementos})
        else:
            try:
                elemento = self.repositorio.buscarPorId(elem_id)
                return jsonify({'resultado': elemento}) 
            except ElementoInexistente:    
                abort(HTTP_404_NOT_FOUND)

    def post(self):
        try:
            elemento = self.repositorio.adicionar(request.json);
            return jsonify({'resultado': elemento}), HTTP_201_CREATED
        except ElementoInvalido:
            abort(HTTP_400_BAD_REQUEST)

    def delete(self, elem_id):
        try:
            self.repositorio.remover(elem_id) 
            return jsonify({'resultado': True})
        except ElementoInexistente:    
            abort(HTTP_404_NOT_FOUND)

    def put(self):
        try:
            elemento = self.repositorio.atualizar(request.json)
            return jsonify({'resultado': elemento})        
        except ElementoInexistente:    
            abort(HTTP_404_NOT_FOUND)

def registrar_api(endpoint, rep, url):
    visao = APIBasica.as_view(endpoint, repositorio=rep)
    app.add_url_rule(url, defaults={'elem_id': None},
        view_func=visao, methods=['GET'])
    app.add_url_rule(url, view_func=visao, methods=['POST','PUT'])
    app.add_url_rule(url+'/<int:elem_id>', view_func=visao, 
        methods=['GET', 'DELETE'])

registrar_api('produto_api', repProdutos, '/app/produtos')
registrar_api('operacao_api', repOperacoes, '/app/operacoes')


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
