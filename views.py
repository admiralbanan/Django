# myapp/views.py
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Person, CarAccident
from .forms import CarAccidentForm

class HomePageView(TemplateView):
    template_name = 'myapp/home.html'

class PersonListView(ListView):
    model = Person
    template_name = 'myapp/person_list.html'
    context_object_name = 'persons'

class CarAccidentListView(ListView):
    model = CarAccident
    template_name = 'myapp/car_accident_list.html'
    context_object_name = 'accidents'

class CarAccidentCreateView(CreateView):
    model = CarAccident
    form_class = CarAccidentForm
    template_name = 'myapp/add_car_accident.html'
    success_url = reverse_lazy('car_accident_list')

class JokesView(TemplateView):
    template_name = 'myapp/jokes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jokes'] = [
            "На границе часовой.\n- Стой, кто идет?\n- Ша, никто уже никуда не идет!",
            # Добавьте остальные анекдоты
        ]
        return context
