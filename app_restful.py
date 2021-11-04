from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Desenvolvedores(Resource):
    def get(self):
        return {'nome': 'Douglas'}
api.add_resource(Desenvolvedores, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)