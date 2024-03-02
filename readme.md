# install django
```bash
pip install django
```
Installing a specific version

```bash
pip install Django==4.2
```

## check installation
```bash
django-admin --version
```

## create a project
```bash
django-admin startproject mysite
```


```bash
django-admin startproject mysite . 
```

## run django

```bash
python manage.py runserver 8000 
```

Open the url http://127.0.0.1:8000/ 

# create apps

```bash
python manage.py startapp blog
python manage.py startapp store
python manage.py startapp task
```

Folders
 - myapp
    - admin.py: for admin panel
    - apps.py: apps configuration
    - models.py: orm tables  write on migrations
    - test.py: 
    - views.py: views to the user
    - urls.py: routing inside the app

## migrations

```bash
python manage.py makemigrations
python manage.py migrate
```    
Create the folling tables:

For Authentication:
 - auth_group
 - auth_group_permissions
 - auth_permission
 - auth_user
 - auth_user_groups
 - auth_user_user_permissions

For django: 
 - django_admin_log
 - django_content_type
 - django_migrations
 - django_session

 ## migrations for an specific app
Add a class into myapp/models.py.
Add the app to the project using the mysite/settings.py in the section INSTALLED_APPS adding myapp and running :

```bash
python manage.py makemigrations myapp
python manage.py migrate myapp
```    
We've created myapp_project table. 