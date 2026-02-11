from flask import Flask
from flask_restx import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes
api = Api(app, version='1.0', title='EndPoint Get', description='Example Restful Service')

SettingName = 'Name'
SettingValue = 'Value'

parserAdd = reqparse.RequestParser()
parserAdd.add_argument(SettingName, type=str, help='Setting Name', required=True)
parserAdd.add_argument(SettingValue, type=str, help='Setting Value', required=True)

mySettingsData = [
            {'Name': 'Setting1', 'Value': 'Value1'},
            {'Name': 'Setting2', 'Value': 'Value2'}
        ]

def getSettingValue(sname):
    for setting in mySettingsData:
        if setting[SettingName] == sname:
            return setting[SettingValue]
    return None

@api.route('/Settings', doc={"description": "Get all settings"})
class GetSettings(Resource):
    def get(self):
        return mySettingsData

@api.route('/Setting', doc={"description": "Add a new setting"})
class AddSetting(Resource):
    @api.doc(parser=parserAdd)
    def post(self):
        args = parserAdd.parse_args()
        sname = args[SettingName]
        svalue = args[SettingValue]
        
        if getSettingValue(sname) != None:
            return {'message': f'Setting {sname} already exists'}, 400
        
        mySettingsData.append({SettingName: sname, SettingValue: svalue})
        return {'message': 'Setting added successfully'}, 201
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=False)