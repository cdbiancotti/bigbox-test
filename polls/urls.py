from django import urls
from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    # generic.DetailView expects the primary key value captured from the URL to be called "pk"
    # that's the reason why we've changed "question_id" to "pk"
    path(r'<int:pk>', views.DetailView.as_view(), name='detail'),
    path(r'<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path(r'<int:question_id>/vote/', views.vote, name='vote'),
]
