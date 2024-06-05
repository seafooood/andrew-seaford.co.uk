from flask import Flask, jsonify
from flask_restx import Resource, Api, reqparse, Namespace
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_jwt_extended.exceptions import NoAuthorizationError
from werkzeug.exceptions import HTTPException
import datetime
import hashlib

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=28800) # Set the life time for the token 
app.config['PROPAGATE_EXCEPTIONS'] = True 

# Create the security manager
jwt = JWTManager(app)
authorizations = {
    'jsonWebToken': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

# Create api
api = Api(app, version='1.0', title='JWT Authorization Example', description='Example Restful Service', authorizations=authorizations, security='jsonWebToken')

# Create and add namespace to the api
ns = Namespace('api', description='API operations', authorizations=authorizations, security='jsonWebToken')
api.add_namespace(ns)

# ##### Secure endpoints #####

@ns.route('/secure')
class SecureData(Resource):
    @jwt_required()
    @ns.doc(security='jsonWebToken')
    def get(self):
        mySecureData = [
            {'Name': 'Setting1', 'Value': 'Value1'},
            {'Name': 'Setting2', 'Value': 'Value2'}
        ]
        return mySecureData

# ##### Unsecure endpoints #####

@ns.route('/unsecure')
class UnsecureData(Resource):
    def get(self):
        myUnsecureData = [
            {'Name': 'Setting3', 'Value': 'Value3'},
            {'Name': 'Setting4', 'Value': 'Value4'}
        ]
        return myUnsecureData

KeyUserName = 'Username'
KeyUserPass = 'Password'
parserUser = reqparse.RequestParser()
parserUser.add_argument(KeyUserName, type=str, help='User Name', required=True)
parserUser.add_argument(KeyUserPass, type=str, help='User Password', required=True)

@ns.route('/login', doc={"description": "User authentication"})
class Login(Resource):
    @api.doc(parser=parserUser)
    def post(self):

        # Get the username and password from the request arguments
        args = parserUser.parse_args()
        username = args[KeyUserName]
        password = args[KeyUserPass]
        
        # Check if the username and password are valid
        if isValidUser(username, password):
            # Log in successful, generate and return access token
            return {'token': create_access_token(identity=username)}, 201

        # Username or password is incorrect, return error
        return {'message': 'Log in failed'}, 401

# ###### User and password validation #####

def isValidUser(username, password):
    """ Validate username and password """
    users = [
            {'Name': 'kyle', 'Password': hash_password('p1')},
            {'Name': 'fred', 'Password': hash_password('p2')}
        ]
    
    for user in users:
        if user['Name'] == username and user['Password'] == hash_password(password):
            return True
    return False

def hash_password(password):
    """hashes password using the SHA-256 algorithm, and returns the hexadecimal representation of the hashed password."""

    # Choose a hashing algorithm (e.g., SHA-256)
    hash_algorithm = hashlib.sha256()
    
    # Encode the password string to bytes
    password_bytes = password.encode('utf-8')
    
    # Update the hash object with the password bytes
    hash_algorithm.update(password_bytes)
    
    # Get the hexadecimal representation of the hashed password
    hashed_password = hash_algorithm.hexdigest()
    
    return hashed_password

# ##### App Entry Point #####
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=False)
