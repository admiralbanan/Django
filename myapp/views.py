from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Person

def person_list(request):
    # Оптимизация запросов
    persons = Person.objects.all().select_related().only(
        'id', 'first_name', 'last_name', 'middle_name', 'passport_series',
        'passport_number', 'birth_date', 'city'
    )

    # Фильтрация
    city = request.GET.get('city')
    if city:
        persons = persons.filter(city__icontains=city)

    last_name = request.GET.get('last_name')
    if last_name:
        persons = persons.filter(last_name__icontains=last_name)

    # Стабильная сортировка для пагинации
    persons = persons.order_by('id')

    paginator = Paginator(persons, 10)
    page_number = request.GET.get('page')
    persons = paginator.get_page(page_number)

    return render(request, 'myapp/person_list.html', {'persons': persons})
