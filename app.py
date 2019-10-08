from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

count = 0

class Counter(Resource):
    def post(self):
        count = count+1
        return count, 200
        
api.add_resource(Counter, "/counter")

app.run(debug=True)
