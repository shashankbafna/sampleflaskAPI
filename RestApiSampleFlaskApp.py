from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import socket
app = Flask(__name__)
api = Api(app)

class Hello(Resource):
	def get(self):
		return jsonify({'message': 'hello world'})
	def post(self):
		data = request.get_json()
		return jsonify({'data': data}), 201

class Square(Resource):
	def get(self,num):
		return jsonify({'number':num,'square':  num**2,'callfrom': socket.getfqdn()})

api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=9299,debug=True,use_reloader=True)
