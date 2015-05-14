# coding=UTF-8
#!flask/bin/python
from flask import Flask, jsonify, request, abort, url_for, send_from_directory
import os

HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_400_BAD_REQUEST = 400
HTTP_404_NOT_FOUND  = 404

class ElementoNaoEncontrado(Exception):
    pass 

class ElementoInvalido(Exception):
    pass 

class Repositorio:
    produtos = []
    def __init__ (self, produtos):
        self.produtos = produtos

    def listar(self):
        return self.produtos

    def buscarPorId(self, prodid):
        resultado = [produto for produto in self.produtos if produto['id'] == prodid]
        if len(resultado) == 0:        
            raise ElementoNaoEncontrado
        return self.produtos        
    
    def remover(self, prodid):
        produto = rep.buscarPorId(prodid);
        self.produtos.remove(produto[0])
        
    def adicionar(self, prod):
        if not (prod and all (k in prod for k in ('nome', 'preco', 'categoria'))):        
            raise ElementoInvalido
        else:
            produto = {
                'id': self.produtos[-1]['id'] + 1,
                'nome': prod['nome'],
                'descricao': prod.get('descricao', ""),
                'preco': prod['preco'],
                'quantidade': prod.get('quantidade', 0),
                'categoria': prod['categoria']
            }
            self.produtos.append(produto)
            return produto;
            
    def atualizar(self, novoprod):
        if novoprod :        
            produto = self.buscarPorId(novoprod['id'])
            produto['nome'] = novoprod.get('nome', produto['nome'])
            produto['descricao'] = novoprod.get('descricao', produto['descricao'])
            produto['preco'] = novoprod.get('preco', produto['preco'])
            produto['quantidade'] = novoprod.get('quantidade', produto['quantidade'])
            produto['categoria'] = novoprod.get('categoria', produto['categoria'])   
            return produto;
        else:
            raise ElementoNaoEncontrado
    
rep = Repositorio([
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


@app.route('/lab/produtos', methods=['GET'])
def list_produtos():
    produtos = rep.listar()
    return jsonify({'produtos': produtos})

@app.route('/lab/produtos/<int:prod_id>', methods=['GET'])
def get_prodduto(prod_id):
    try:
        produto = rep.buscarPorId(prod_id)
        return jsonify({'produto': produto}) 
    except ElementoNaoEncontrado:    
        abort(HTTP_404_NOT_FOUND)

@app.route('/lab/produtos/', methods=['POST'])
def create_prod():
    try:
        produto = rep.adicionar(request.json);
        return jsonify({'produto': produto}), HTTP_201_CREATED
    except ElementoInvalido:
       abort(HTTP_400_BAD_REQUEST)

@app.route('/lab/produtos/<int:prod_id>', methods=['PUT'])
def update_produto(prod_id):
    try:
        produto = rep.atualizar(request.json)
        return jsonify({'task': produto})        
    except ElementoNaoEncontrado:    
        abort(HTTP_404_NOT_FOUND)

@app.route('/lab/produtos/<int:prod_id>', methods=['DELETE'])
def delete_task(prod_id):
    try:
        rep.remover(prod_id) 
        return jsonify({'result': True})
    except ElementoNaoEncontrado:    
        abort(HTTP_404_NOT_FOUND)


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
