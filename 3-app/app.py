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

repProdutos = RepositorioProdutos()
repOperacoes = RepositorioOperacoes(repProdutos)

app = Flask(__name__, static_folder='static', static_url_path='/ui')
    

@app.route("/")
def root():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/app/produtos', methods=['GET'])
def list_Produtos():
    produtos = repProdutos.listar()
    return jsonify({'resultado': produtos})

@app.route('/app/produtos/<int:prod_id>', methods=['GET'])
def get_prodduto(prod_id):
    try:
        produto = repProdutos.buscarPorId(prod_id)
        return jsonify({'resultado': produto}) 
    except ElementoInexistente:    
        abort(HTTP_404_NOT_FOUND)

@app.route('/app/produtos', methods=['POST'])
def create_prod():
    try:
        produto = repProdutos.adicionar(request.json);
        return jsonify({'resultado': produto}), HTTP_201_CREATED
    except ElementoInvalido:
       abort(HTTP_400_BAD_REQUEST)

@app.route('/app/produtos/<int:prod_id>', methods=['PUT'])
def update_produto(prod_id):
    try:
        produto = repProdutos.atualizar(request.json)
        return jsonify({'resultado': produto})        
    except ElementoInexistente:    
        abort(HTTP_404_NOT_FOUND)

@app.route('/app/produtos/<int:prod_id>', methods=['DELETE'])
def delete_produto(prod_id):
    try:
        repProdutos.remover(prod_id) 
        return jsonify({'resultado': True})
    except ElementoInexistente:    
        abort(HTTP_404_NOT_FOUND)


@app.route('/app/operacoes', methods=['GET'])
def list_operacoes():
    operacoes = repOperacoes.listar()
    return jsonify({'resultado': operacoes})

@app.route('/app/operacoes/<int:op_id>', methods=['GET'])
def get_operacao(op_id):
    try:
        operacao = repOperacoes.buscarPorId(op_id)
        return jsonify({'resultado': operacao}) 
    except ElementoInexistente:    
        abort(HTTP_404_NOT_FOUND)

@app.route('/app/operacoes', methods=['POST'])
def create_operacao():
    try:
        operacao = repOperacoes.adicionar(request.json);
        return jsonify({'resultado': operacao}), HTTP_201_CREATED
    except ElementoInvalido:
       abort(HTTP_400_BAD_REQUEST)

@app.route('/app/operacoes', methods=['PUT'])
def update_operacao():
    try:
        operacao = repOperacoes.atualizar(request.json)
        return jsonify({'resultado': operacao})        
    except ElementoInexistente:    
        abort(HTTP_404_NOT_FOUND)

@app.route('/app/operacoes/<int:op_id>', methods=['DELETE'])
def delete_operacao(op_id):
    try:
        repOperacoes.remover(op_id) 
        return jsonify({'resultado': True})
    except ElementoInexistente:    
        abort(HTTP_404_NOT_FOUND)


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
