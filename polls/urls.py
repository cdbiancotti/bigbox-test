from django import urls
from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'<int:question_id>', views.detail, name='detail'),
    path(r'<int:question_id>/results/', views.results, name='results'),
    path(r'<int:question_id>/vote/', views.vote, name='vote'),
]
