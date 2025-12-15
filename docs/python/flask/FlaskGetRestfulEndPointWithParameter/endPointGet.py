from flask import Flask
from flask_restx import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes
api = Api(app, version='1.0', title='EndPoint Get', description='Example Restful Service')

mySettingsData = [
            {'Name': 'Setting1', 'Value': 'Value1'},
            {'Name': 'Setting2', 'Value': 'Value2'}
        ]

def getSettingValue(sname):
    for setting in mySettingsData:
        if setting['Name'] == sname:
            return setting['Value']
    return None

@api.route('/Settings', doc={"description": "Get all settings"})
class GetSettings(Resource):
    def get(self):
        return mySettingsData

@api.route('/Setting/<string:sname>', doc={"description": "Get one setting value"})
@api.param('sname', 'Setting Name')
class GetSetting(Resource):
    def get(self, sname):
        value = getSettingValue(sname)
        if value == None:
            return {'message': f'Invalid setting name. {sname} does not exist'}, 400
        else:
            return value
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=False)