# Meta Backend Developper Final Project
Meta Capstone project for the Backend developer program

## URls routes

```
restaurant/
restaurant/menu/items/
restaurant/menu/items/<pk>
restaurant/booking/tables/
restaurant/booking/tables/<pk>
restaurant/api-token-auth/
admin/
auth/users/
auth/token/login
```

## Database configuration
Create .env file in root folder with those environment variable. Must match the database credentials.

```
DB_Name=<Database Name>
DB_Host=<Hostname or IP>
DB_Port=<Database Port>
DB_User=<Database Username>
DB_Password=<Database Password>

```

## Database user permissions
If you are using different database user than the root user, you should set the permission for test database.
```
Allowing django-admin user to access test_* database (test_ followed by any characters)
grant all privileges on `test\_%`.* to 'django-admin'@'localhost'

````

## Installing the project dependencies
```
cd <project directory>

pipenv shell

pipenv install -r ./requirements.txt

python manage.py check

python manage.py makemigrations

python manage.py migrate

python manage.py runserver


````




