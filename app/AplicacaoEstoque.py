# coding=UTF-8
#!flask/bin/python
from flask import Flask, jsonify, request, abort, url_for, send_from_directory
from produtos import RepositorioProdutos,ProdutoNaoEncontrado,ProdutoInvalido
import os

HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_400_BAD_REQUEST = 400
HTTP_404_NOT_FOUND  = 404

rep = RepositorioProdutos([
            {
                'id': 1,
                'nome':  u"Blu-ray - O exterminador do Futuro",
                'descricao': u"Andróide (Arnold Schwarzenegger) vem do futuro com o objetivo de matar a mãe (Linda Hamilton) de um futuro líder guerrilhero humano.",
                'preco': 22.41,
        		'quantidade': 10,
        		'categoria' : "DVD"
            },
            {
                'id': 3,
                'nome': u"Exterminador de cupins 400ml",
                'descricao': u"O exterminador de cupins", 
                'preco': 19.33,
        		'quantidade': 30,
        		'categoria' :  "limpeza"
            },	
        	{
                'id': 4,
                'nome': u"Fantasia Adulto Exterminador John Connor",
                'descricao': u"Transforme-se em seu heroi", 
                'preco': 300.85,
        		'quantidade': 3,
        		'categoria' :  "fantasia"
            }	
        ])
    
app = Flask(__name__, static_folder='static', static_url_path='/ui')
    

@app.route("/")
def root():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/app/produtos', methods=['GET'])
def list_():
    produtos = rep.listar()
    return jsonify({'produtos': produtos})

@app.route('/app/produtos/<int:prod_id>', methods=['GET'])
def get_prodduto(prod_id):
    try:
        produto = rep.buscarPorId(prod_id)
        return jsonify({'produto': produto}) 
    except ProdutoNaoEncontrado:    
        abort(HTTP_404_NOT_FOUND)

@app.route('/app/produtos', methods=['POST'])
def create_prod():
    try:
        produto = rep.adicionar(request.json);
        return jsonify({'produto': produto}), HTTP_201_CREATED
    except ProdutoInvalido:
       abort(HTTP_400_BAD_REQUEST)

@app.route('/app/produtos/<int:prod_id>', methods=['PUT'])
def update_produto(prod_id):
    try:
        produto = rep.atualizar(request.json)
        return jsonify({'task': produto})        
    except ProdutoNaoEncontrado:    
        abort(HTTP_404_NOT_FOUND)

@app.route('/app/produtos/<int:prod_id>', methods=['DELETE'])
def delete_task(prod_id):
    try:
        rep.remover(prod_id) 
        return jsonify({'result': True})
    except ProdutoNaoEncontrado:    
        abort(HTTP_404_NOT_FOUND)


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
