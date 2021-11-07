import json
from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, AlteraHabilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores =\
    [
    {'id':'0',
     'nome': 'Douglas',
     'habilidades':['Python', 'Flask']
     },
    {'id':'1',
     'nome': 'Peron',
     'habilidades':['Python', 'Django']}
     ]
#devolve um Dev pelo ID, altera e deleta um DEV
class Desenvolvedores(Resource):
    def get(self, id):
            try:
                response = desenvolvedores[id]
            except IndexError:
                mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
                response = {'status': 'erro', 'mensagem': mensagem}
            except Exception:
                mensagem = 'Erro desconhecido. Procure o ADM da API'
                response = {'status': 'erro', 'mensagem': mensagem}
            return response
    def put(self):
        dados = json.load(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excludo'}
#lista todos os DEV, inclui novo DEV
class ListaDesenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    def get(self):
        return desenvolvedores



api.add_resource(Desenvolvedores, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(AlteraHabilidades, '/habilidades/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)