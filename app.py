from flask import Flask
from flask_restful import Api
from resources import Main

# Create Flask App
app = Flask(__name__)
api = Api(app)
# Routes
api.add_resource(Main, '/')
# Run App
if __name__ == '__main__':
	app.run(debug=True)