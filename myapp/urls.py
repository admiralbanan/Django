from django.urls import path
from myapp.views import (
    PersonListView,
    CarAccidentListView,
    CarAccidentCreateView,
    HomePageView,
    JokesView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('persons/', PersonListView.as_view(), name='person_list'),
    path('accidents/', CarAccidentListView.as_view(), name='car_accident_list'),
    path('add-accident/', CarAccidentCreateView.as_view(), name='add_car_accident'),
    path('jokes/', JokesView.as_view(), name='jokes'),  # Новый URL для анекдотов
]
