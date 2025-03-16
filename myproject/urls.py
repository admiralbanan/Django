from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Убираем дополнительный 'persons/'
    path('', lambda request: redirect('person_list', permanent=False)),  # Перенаправление с корня на /persons/
]
