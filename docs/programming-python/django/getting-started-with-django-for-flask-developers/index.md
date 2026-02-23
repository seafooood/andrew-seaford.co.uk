---
keywords: [django, flask migration, python web framework, getting started, tutorial]
---

# Getting Started with Django for Flask Developers

## Introduction

If you're familiar with Python and have experience with Flask, picking up Django will be much easier. Django is a high-level web framework that promotes rapid development and clean, pragmatic design. It follows the "batteries-included" philosophy, providing built-in tools for authentication, ORM, admin interfaces, and more.

This guide will help you transition from Flask to Django by covering:

- Installing Django
- Creating a Django Project
- Understanding Django’s Project Structure
- Running the Development Server
- Creating and Managing Apps
- Handling Routes and Views
- Working with Templates
- Using the ORM and Database Migrations
- Admin Interface

## 1. Installing Django

Ensure you have Python installed (>= 3.8 recommended). Install Django using pip:

```bash
pip install django
```

Verify installation:

```bash
django-admin --version
```

## 2. Creating a Django Project

Unlike Flask, where you structure your project manually, Django provides a command to scaffold a project:

```bash
django-admin startproject myproject
cd myproject
```

This creates a Django project with a default structure.

## 3. Understanding Django’s Project Structure

A newly created Django project looks like this:

```less
myproject/
│── manage.py       # CLI tool for Django commands
│── myproject/      # Main project directory
│   │── __init__.py
│   │── settings.py # Configuration (like Flask’s app.config)
│   │── urls.py     # URL routing (similar to Flask's @app.route)
│   │── asgi.py
│   │── wsgi.py
```

manage.py – Used to run commands like migrations, running the server, etc.
settings.py – Contains project settings like database configurations, installed apps, and middleware.
urls.py – Defines URL patterns for the project, similar to Flask’s routing system.

## 4. Running the Development Server

Start the built-in development server:

```bash
python manage.py runserver
```

By default, Django runs on [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Visit this URL to see Django's welcome page.

## 5. Creating and Managing Apps

Django projects are divided into apps (similar to Flask blueprints). Create an app with:

```bash
python manage.py startapp myapp
```

This creates:

```less
myapp/
│── migrations/      # Database migrations
│── __init__.py
│── admin.py         # Admin panel configuration
│── apps.py
│── models.py        # Database models
│── tests.py
│── views.py         # View functions (like Flask routes)
```

Register the app in settings.py:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'myapp',  # Add this line
]
```


##6. Handling Routes and Views

In Flask, you define routes using @app.route(). In Django, routes are defined in urls.py and connected to views.

Define a view (myapp/views.py):

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```

Configure the URL (myapp/urls.py):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

Include the app’s URLs in the project’s urls.py:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include app routes
]
```

Now, visiting [http://127.0.0.1:8000/](http://127.0.0.1:8000/) will show "Hello, Django!".

## 7. Working with Templates

Django’s template system is more powerful than Flask’s Jinja, but syntax is similar.

Create a templates folder inside myapp:

```less
myapp/
│── templates/
│   │── home.html
```

Create a template (myapp/templates/home.html):

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Django App</title>
</head>
<body>
    <h1>Welcome to Django</h1>
</body>
</html>
```

Modify the view to use the template:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

Now, [http://127.0.0.1:8000/](http://127.0.0.1:8000/) will render home.html.

## 8. Using the ORM and Database Migrations

Django has a built-in ORM, unlike Flask which requires SQLAlchemy separately.

Define a Model (myapp/models.py):

```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
```

Apply Migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Use Django’s Shell to Test:

```bash
python manage.py shell
```

```python
from myapp.models import Item
Item.objects.create(name="Laptop", description="A powerful laptop")
Item.objects.all()
```

## 9. Django Admin Interface

Django includes an admin panel for managing data.

Enable Admin:
Modify myapp/admin.py:

```python
from django.contrib import admin
from .models import Item

admin.site.register(Item)
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the server and log in at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Summary: Flask vs Django

|Feature|Flask|Django
|-|-|-
|Project Structure|Minimal, flexible|Structured, batteries-included
|Routing|@app.route|urls.py and path()
|Templates|Jinja2|Django Templates (Jinja-like)
|ORM|SQLAlchemy (optional)|Built-in ORM
|Admin Panel|None by default|Built-in

Django is more structured and opinionated, which speeds up development for complex applications. If you’re comfortable with Flask, Django will take some getting used to, but its features can greatly improve productivity.


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/django/getting-started-with-django-for-flask-developers](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/django/getting-started-with-django-for-flask-developers)

## Python Related Articles

- ['django-admin startproject' vs 'python -m django startproject'](../'django-admin-startproject'-vs-'python-m-django-startproject'/index.md)
- [Creating a Django Site With User Authentication](../creating-a-django-site-with-user-authentication/index.md)
- [Django Database Seeding](../django-database-seeding/index.md)
- [Getting Started with Django - Working with Databases](../getting-started-with-django-working-with-databases/index.md)
- [How to Start a Django Project](../how-to-start-a-django-project/index.md)
