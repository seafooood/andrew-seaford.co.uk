from flask_restx import Namespace, Resource, Api, fields, reqparse
from flask import Flask, request

databaseName = "bob1.db"
app = APIFlask(__name__)


@app.get('/categorytest')
def GetCategory(self):
    return "bob"

api = Api(app)
api = Namespace('Categories', description='System Settings Endpoint')