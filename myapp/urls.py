# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.person_list, name='person_list'),  # URL для списка людей
]
