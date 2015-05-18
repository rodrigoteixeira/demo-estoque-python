# coding=UTF-8
from flask import Flask, jsonify, request, abort, url_for
from flask.views import MethodView
from app_estoque.modelo import ElementoInexistente, ElementoInvalido

HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_400_BAD_REQUEST = 400
HTTP_404_NOT_FOUND  = 404

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

