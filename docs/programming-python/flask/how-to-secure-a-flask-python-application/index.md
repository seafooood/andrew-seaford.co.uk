---
title: "How To Secure A Flask Python Application"
keywords: [flask, JWT authentication, python, API security, token-based auth]
date: 2025-02-02
categories:
  - "prog"
  - "python"
---

## Introduction

Securing a Python Flask application with JWT authentication is crucial for safeguarding sensitive data and ensuring user privacy and security. JWT (JSON Web Tokens) authentication offers a lightweight, stateless mechanism for verifying the identity of clients accessing the application. By implementing JWT authentication, developers can prevent unauthorized access to resources and endpoints within the Flask application.

JWT authentication adds an extra layer of security by generating tokens that contain encoded user information, which can be securely transmitted between the client and the server. These tokens are signed with a secret key, making them tamper-proof and resistant to unauthorized alterations. With JWT, developers can enforce access controls, validate the integrity of incoming requests, and manage user sessions efficiently without relying on server-side storage.

Furthermore, JWT authentication enhances scalability and performance by eliminating the need for server-side session management, reducing the burden on server resources. This approach also promotes interoperability, allowing different services and platforms to authenticate users seamlessly using standardized JWT tokens. Overall, securing a Python Flask application with JWT authentication helps mitigate security risks, enhances user experience, and ensures compliance with modern security standards.

In this article, we are going to secure a simple Python Flask application backend and build a simple HTML frontend that will make requests to the backend.

## The Backend

The backend Python Flask application hosts three endpoints.

- GET /api/unsecure
    
    The Unsecured endpoint returns data without authorization.
    
- GET /api/secure
    
    The secure endpoint requires authorization
    
- POST /api/login
    
    The login endpoint validates a user's credentials and returns an access token.
    

### Creating The Backend Application

- Create a text file called `backend.py` and enter the code from backend.py.
- From the terminal, install the required libraries

```bash
pip install flask
pip install flask_restx
pip install flask_cors
pip install flask_jwt_extended
```

### Testing The Backend Application

- From the terminal execute the Python application `python backend.py`
    
- The console output from the Python application will display the server address. In this example, the backend is hosted at http://127.0.0.1:5500
    
- Open a web browser and navigate to http://127.0.0.1:5500
    
- The web browser will show the Swagger page for the backend. Click _api_ to display the endpoints.
    
- Test the unsecure endpoint
    
    - Click the _GET_ next to /api/unsecure
    - Click _Try it out_ button
    - Click _Execute_ button
    - The _Response Body_ will display the JSON response from the GET request.
- Test the secure endpoint without authorization
    
    - Click the _GET_ next to /api/secure
    - Click _Try it out_ button and then click the _Execute_ button. The _Response Body_ will display the message "Missing Authorization Header".
- Generate Authorization Token
    
    - Click _POST_ next to /api/login
    - Click the _Try it out_ button
    - Enter the username _kyle_, password _p1_ and click the _Execute_ button.
    - Copy the access token from the _Response Body_.
- Test the secure endpoint with authentication
    
    - Click the padlock icon on the right hand side of _GET_ /api/secure
    - Enter _Bearer_ into the value text box followed by the access token, then click the _Authorize_ button.
    - Click the _Close_ button to close the authorization window.
    - Click the _Execute_ button, this time the _Response Body_ should show the JSON data from the request.

### Endpoint Authentication

The main difference between the definitions for the secure and unsecure endpoints are the function decorators.

Unsecure endpoint

```python
@ns.route('/unsecure')
class UnsecureData(Resource):
    def get(self):
```

Secure endpoint, note the function decorators `@jwt_required()` and `@ns.doc(security='jsonWebToken')`. The decorators enforce that the request header must contain the access token.

```python
@ns.route('/secure')
class SecureData(Resource):
    @jwt_required()
    @ns.doc(security='jsonWebToken')
    def get(self):
```

## The Frontend

### Creating The Frontend Application

- Create a text file called `frontend.html` and enter the code from frontend.html.

### Testing The Frontend Application

- Using a web browser open the file `frontend.html`
    
- Enter the username _kyle_, password _p1_ and then click the _Log In_ button.
    
- Click the _OK_ button to confirm the successful login.
    
- Click the _Get Secure Data_ button, the JSON response data will be displayed below the button.
    

## Summary

In this solution, no user credentials are stored in the front end. The backend validates the user's name and password and returns a temporary access token, the access token is used to authorize requests to the backend endpoints.


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/flask/how-to-secure-a-flask-python-application](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/flask/how-to-secure-a-flask-python-application)

## Python Related Articles

- ['django-admin startproject' vs 'python -m django startproject'](../../django/'django-admin-startproject'-vs-'python-m-django-startproject'/index.md)
- [Creating a Django Site With User Authentication](../../django/creating-a-django-site-with-user-authentication/index.md)
- [Django Database Seeding](../../django/django-database-seeding/index.md)
- [Getting Started with Django for Flask Developers](../../django/getting-started-with-django-for-flask-developers/index.md)
- [Getting Started with Django - Working with Databases](../../django/getting-started-with-django-working-with-databases/index.md)
