from django.urls import path
from . import views

app_name = 'bigbox'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'box/', views.boxes, name='boxes'),
    path(r'box/<int:box_id>', views.box, name='box_detail'),
    path(r'box/<str:box_slug>', views.box_by_slug, name='box_by_slug'),
    path(r'box/<int:box_id>/activity',
         views.box_activities, name='box_activities'),
    path(r'box/<int:box_id>/activity/<int:activity_id>',
         views.activity, name='activity_detail'),
]
