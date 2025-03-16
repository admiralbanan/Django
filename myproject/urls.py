from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Убираем дополнительный 'persons/'
    path('', lambda request: redirect('person_list', permanent=False)),  # Перенаправление с корня на /persons/
]

# Добавляем debug_toolbar, только если DEBUG=True
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
