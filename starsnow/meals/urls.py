from django.urls import path
from . import views

app_name = 'meals'

urlpatterns = [
    path('',views.home, name = 'starsnowice-home'),
    path('meals/', views.meal_list, name = 'meal_list'),
    path('meals/<slug:slug>',views.meal_detail, name='meal_detail'),
    path('location/', views.location, name = 'location'),
    ]
