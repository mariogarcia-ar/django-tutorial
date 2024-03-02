from django.urls import path
# My App
from . import views

urlpatterns = [
    path("", views.index),
    path("hello/<str:username>", views.hello),
    path("about", views.about),
    path("projects", views.projects),
    path("create_project", views.create_project),
    path("tasks", views.tasks),
    path("create_task", views.create_task),
]
