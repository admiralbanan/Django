# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('persons/', views.person_list, name='person_list'),
    path('accidents/', views.car_accident_list, name='car_accident_list'),
    path('add-accident/', views.add_car_accident, name='add_car_accident'),  # Новый URL для формы
]