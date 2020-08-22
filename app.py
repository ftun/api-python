from flask import Flask
from flask_restful import Resource, Api
from resources.Hello import Hello

app = Flask(__name__)
api = Api(app)

api.add_resource(Hello, '/')

if __name__ == '__main__':
    app.run(debug=True)
