# Shopping Django App
## About
This is a web app of a shopping list application that allows users to record things they want
to purchase and keep track of their shopping. This APP is developed using the Django Framework.
Find Staging site [here](https://django-shopping-list.herokuapp.com)
## Features
With this APP;
- You can create a user account - ```/signup/```
- You can login and log out - ```/login/``` & ```/logout/```
- You can reset your password - ```/reset/```
- You can create, view, update, and delete a shopping list in your user account
- You can create, view, update, and delete an item in your shopping list under your account
## Technology stack
Tools used during the development of this API are;
- [Python 3](https://www.python.org) - Programming Language
- [Django](https://www.djangoproject.com) - a python web framework
- [Postgresql](https://www.postgresql.org/) - this is a database server
## Requirements
- Use Python 3.x.x+
- Use Django 2.x.x+
## Running the application
To run this application, clone the repository on your local machine and execute the following command.
```sh
    $ git clone https://github.com/parseendavid/django-shopping-list.git
    $ cd django-shopping-list
    $ virtualenv virtenv
    $ source virtenv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
```
#### Endpoints to create a user account and login into the application
|End point | Public Access|Action
|----------|--------------|------
/signup | True | Create an account
/login | True | Login a user
/logout | False | Logout a user
/reset-password | False | Reset a user password

#### Endpoints to create, update, view and delete a shopping list & it's items
|End point | Public Access|Action
|----------|--------------|------
/dashboard | False | Create, Read, Update and Delete a shopping list
/details/<int:list_id> | False | View all shopping list's items
/details/<int:list_id>/<int:item_id> | False | Update and Delete a shopping list's item
