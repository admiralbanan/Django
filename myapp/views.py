from .models import Person
from .models import CarAccident
from django.shortcuts import render, redirect
from .forms import CarAccidentForm
from django.contrib import messages  # Импортируем messages

def person_list(request):
    persons = Person.objects.all()  # Получаем всех людей из базы данных
    return render(request, 'myapp/person_list.html', {'persons': persons})
def car_accident_list(request):
    accidents = CarAccident.objects.all()
    return render(request, 'myapp/car_accident_list.html', {'accidents': accidents})
def home(request):
    return render(request, 'myapp/home.html')
def add_car_accident(request):
    if request.method == 'POST':
        form = CarAccidentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Инцидент успешно добавлен!')
            return redirect('car_accident_list')  # Перенаправляет на список инцидентов
    else:
        form = CarAccidentForm()
    return render(request, 'myapp/add_car_accident.html', {'form': form})