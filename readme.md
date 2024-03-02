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

# Shell

```bash
python manage.py shell
```   

```python
from myapp.models import Project, Task

# create a project
p = Project(name="application movil")
p.save()

p = Project(name="application web")
p.save()

# list projects
Project.objects.all()

# find by id
Project.objects.get(id=2)
# find by name
Project.objects.get(name="application movil")

```   

```python
from myapp.models import Project, Task

# find by id
p = Project.objects.get(id=2)

# create a task
t = Task(title="tarea 1", description="una tarea", project=p)
t.save()

# list all task for a project
p.task_set.all()

# other way
p.task_set.create(title="tarea 2", description="otro tarea")

# get a task from a project
p.task_set.get(id=1)

# usign filters
Project.objects.filter(name__startswith="appli")
```   

# Params


# Admin Panel
Go to  http://127.0.0.1:8000/admin/ 


Create a super user
```bash
python manage.py createsuperuser
```   

Add Project and task editing myapp/admin.py
Now you and navigate to http://127.0.0.1:8000/admin/myapp/project/

# Templates
