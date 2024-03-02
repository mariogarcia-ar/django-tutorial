from django.urls import path
# My App
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hello/<str:username>", views.hello, name="hello"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("create_project", views.create_project, name="project_create"),
    path("tasks", views.tasks, name="tasks"),
    path("create_task", views.create_task, name="task_create"),
]
