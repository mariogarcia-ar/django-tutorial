from django.urls import path
# My App
from . import views

urlpatterns = [
    path("", views.hello),
    path("about", views.about),
]
