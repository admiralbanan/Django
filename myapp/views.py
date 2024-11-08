# myapp/views.py
from django.shortcuts import render
from .models import Person

def person_list(request):
    persons = Person.objects.all()  # Получаем всех людей из базы данных
    return render(request, 'myapp/person_list.html', {'persons': persons})
