#!flask/bin/python
from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

with open("json\lab_produtos.json") as json_file:
    produtos = json.load(json_file)
    print(produtos)

@app.route('/lab/produtos', methods=['GET'])
def list_produtos():
    return jsonify({'produtos': produtos})

@app.route('/lab/produtos/<int:prod_id>', methods=['GET'])
def get_prodduto(prod_id):
    produto = [produto for produto in produtos if produto['id'] == prod_id]
    if len(produto) == 0:
        abort(404)
    return jsonify({'produto': produto[0]})

@app.route('/lab/produtos/', methods=['POST'])
def create_prod():
    if not request.json and not all (k in request.json for k in ('nome', 'preco', 'categoria')):
       abort(400)
    produto = {
        'id': produtos[-1]['id'] + 1,
        'nome': request.json['nome'],
        'descricao': request.json.get('descricao', ""),
        'preco': request.json['preco'],
        'quantidade': request.json.get('quantidade', 0),
        'categoria': request.json['categoria']
    }
    produtos.append(produto)
    return jsonify({'produto': produto}), 201

@app.route('/lab/produtos/<int:prod_id>', methods=['PUT'])
def update_produto(prod_id):
    produto = [produto for produto in produtos if produto['id'] == prod_id]
    if len(produto) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'nome' in request.json and type(request.json['nome']) != str:
        abort(400)
    if 'descricao' in request.json and type(request.json['descricao']) is not str:
        abort(400)
    if 'preco' in request.json and type(request.json['preco']) is not int:
        abort(400)
    if 'quantidade' in request.json and type(request.json['quantidade']) is not int:
        abort(400)
    if 'categoria' in request.json and type(request.json['categoria']) is not int:
        abort(400)
    produto[0]['nome'] = request.json.get('nome', produto[0]['nome'])
    produto[0]['descricao'] = request.json.get('descricao', produto[0]['descricao'])
    produto[0]['preco'] = request.json.get('preco', produto[0]['preco'])
    produto[0]['quantidade'] = request.json.get('quantidade', produto[0]['quantidade'])
    produto[0]['categoria'] = request.json.get('categoria', produto[0]['categoria'])
    return jsonify({'task': produto[0]})

@app.route('/lab/produtos/<int:prod_id>', methods=['DELETE'])
def delete_task(prod_id):
    produto = [produto for produto in produtos if produto['id'] == prod_id]
    if len(produto) == 0:
        abort(404)
    produtos.remove(produto[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
