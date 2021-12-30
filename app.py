from flask import Flask
from flask_restful import Resource, Api, reqparse

# Initialize App object from Flask
app = Flask(__name__)
api = Api(app)

# Create Resource

class User(Resource):

	# api/users
	def get(self):
		# Do some stuff here
		return {"msg": "successful first api call! 🎉"}

	def post(self):
		'''
		api/users
		{
			"name": "Alex",
			"email": "alex@cc.com"
		}
		'''
		parser = reqparse.RequestParser()
		parser.add_argument('name', location='json')
		parser.add_argument('email', location='json')
		args = parser.parse_args()

		print("ARGS from BODY in JSON FORMAT: ", args)

		return {}

class UserWithQuery(Resource):

	# api/users?month=12-2021
	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('month')
		query_params_dict = parser.parse_args()
		return {}

	def post(self):
		'''
		api/users-with-query
			name = "Alex"
			email = "alex@cc.com"
		'''
		parser = reqparse.RequestParser()
		parser.add_argument('name', location='form')
		parser.add_argument('email', location='form')
		args = parser.parse_args()

		print("ARGS from BODY in JSON FORMAT: ", args)

		return {}


class UserWithSlash(Resource):

	# api/users/23456
	def get(self, u_id):
		print("Userd ID:", u_id)
		return {}

# Create endpoint
api.add_resource(User, '/api/users')
api.add_resource(UserWithQuery, '/api/users-with-query')
api.add_resource(UserWithSlash, '/api/users-with-slash/<int:u_id>')


if __name__ == '__main__':
	# Run Flask-server
	app.run()

