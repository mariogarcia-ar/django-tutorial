from django.urls import path
# My App
from . import views

urlpatterns = [
    path("", views.index),
    path("hello/<str:username>", views.hello),
    path("about", views.about),
    path("projects", views.projects),
    path("tasks", views.tasks),
]
