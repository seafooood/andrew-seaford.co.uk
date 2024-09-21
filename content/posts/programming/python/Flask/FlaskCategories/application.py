from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from endpoint_categories import api as namespaceCategories
from endpoint_categories import Categories

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes
api = Api(app, version='1.0', title='Application', description='Application Swagger')
api.add_namespace(namespaceCategories)

if __name__ == '__main__':
    Categories("Categories.db")
    app.run(host='0.0.0.0', port=5500, debug=False)