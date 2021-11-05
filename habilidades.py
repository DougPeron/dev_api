import json

from flask import request
from flask_restful import Resource


lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    def post(self):
        nova_habilidade = json.loads(request.data)
        lista_habilidades.append(nova_habilidade)
        return lista_habilidades

class AlteraHabilidades (Resource):
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return lista_habilidades
    def get(self, id):
        return lista_habilidades[id]
    def delete(self, id):
        lista_habilidades.pop(id)
        return lista_habilidades
