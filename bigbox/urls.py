from django.urls import path
from . import views

# app_name = 'bigbox'

urlpatterns = [
    path('', views.index, name='index'),
    path('box/', views.boxes, name='boxes'),
    path('box/<int:box_id>', views.box, name='box_detail'),
    path('box/<str:box_slug>', views.box_by_slug, name='box_by_slug'),
    path('box/<int:box_id>/activity', views.box_activities, name='box_activities'),
    path('box/<int:box_id>/activity/<int:activity_id>',
         views.activity, name='activity_detail'),
]
