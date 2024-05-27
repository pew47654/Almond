# Almonds
### This repository is used for the Senior Project named Almonds.
Almonds is a database hub used by organizations to generate metadata following the DGA metadata format, making the organization's database more explorable.

## Install package components
This is for command prompt or terminal
### Back-end:
_**Navigate to backend folder first_
```
$ cd backend
```
```
$ pip install -r requirements.txt
```
### Front-end:
_**Navigate to frontend folder first_
```
$ cd frontend
```
```
$ npm install axios react-router-dom jwt-decode
```

## Database setup
### Example for PostgreSQL:
_backend/backend/settings.py_
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_name',
        'USER': 'user_name',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
## You need to care about '.env' file between two main folder (frontend and backend)
Create by yourself in main folder.
### backend .env example:
used with the settings.py
``` 
#POSTGRESQL
DB_NAME_POSTGRES = database_postgresql
DB_USER_POSTGRES = postgres
DB_PASSWORD_POSTGRES = 1111      
DB_HOST_POSTGRES = localhost
DB_PORT_POSTGRES = 5432

#MYSQL
DB_NAME_MYSQL = database_mysql
DB_USER_MYSQL = root
DB_PASSWORD_MYSQL = 1111
DB_HOST_MYSQL = localhost
DB_PORT_MYSQL = 3306

#MONGODB
DB_URL_MONGO = mongodb+srv://tiger10147:1111@cluster0.mwscnaj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
```
### frontend .env example:
used with the api.js file
``` 
VITE_API_URL = http://127.0.0.1:8000/
```

## Migrate the models (database tables) from Django to PostgreSQL (database).
In Django, you can write a model file to define database tables and use commands to create those tables in the database.
### The command to migrate Django models to the database:
_**Don't forget to navigate to backend folder_
```
$ python manage.py makemigrations
$ python manage.py migrate
```
## Reference for more information:
**Back-end**
1. [Django](https://docs.djangoproject.com/en/5.0/)

**Front-end**
1. [React](https://legacy.reactjs.org/docs/getting-started.html)
2. [JWT](https://jwt.io/introduction)


## Features checklists
Feature | Description | |
-----|-----|-----|
Database Connection|Adding support for more database platforms. Previously, only PostgreSQL was supported; now, we are adding MySQL and MongoDB.|:white_check_mark:
Data Catalog|Lists all database connection details for better exploration.|:white_check_mark:
Data Overview|Lists each database's information and all tables within the database.|:white_check_mark:
Metadata|Displays metadata with a description field for each attribute to provide details.|:white_check_mark:
Generate ER-Diagram|Generate an ER-diagram.|:x:

## Demo
https://youtu.be/E8xurB1a3dI
