from django import urls
from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path(r'', views.index, name='index')
]
