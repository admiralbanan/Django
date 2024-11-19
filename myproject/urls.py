# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Подключение путей accounts
    path('accounts/', include('django.contrib.auth.urls')),  # URL-адреса для авторизации
    path('', include('myapp.urls')),  # Подключаем маршруты из myapp
]
