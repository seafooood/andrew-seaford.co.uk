from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from categories import api as namespaceCategories

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes
api = Api(app, version='1.0', title='Application', description='Application Swagger')

api.add_namespace(namespaceCategories)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=False)