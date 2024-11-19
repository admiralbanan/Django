# myapp/forms.py
from django import forms
from .models import CarAccident
from django.utils import timezone

class CarAccidentForm(forms.ModelForm):
    class Meta:
        model = CarAccident
        fields = ['brand', 'license_plate', 'year_of_manufacture', 'last_accident_date', 'compensation_amount', 'passengers_injured']

    # Опции для поля "Марка автомобиля"
    CAR_BRANDS = [
        ("Lada", "Lada"), ("Gaz", "Gaz"), ("Kamaz", "Kamaz"), ("BMW", "BMW"),
        ("Mercedes", "Mercedes"), ("Audi", "Audi"), ("Volkswagen", "Volkswagen"),
        ("Renault", "Renault"), ("Peugeot", "Peugeot"), ("Opel", "Opel"),
        ("Skoda", "Skoda"), ("Fiat", "Fiat")
    ]
    brand = forms.ChoiceField(choices=CAR_BRANDS, label="Марка автомобиля")

    # Годы выпуска от 2001 до 2024
    YEAR_CHOICES = [(year, year) for year in range(2001, 2025)]
    year_of_manufacture = forms.ChoiceField(choices=YEAR_CHOICES, label="Год выпуска")

    # Даты в пределах последнего года
    DATE_CHOICES = [
        (timezone.now() - timezone.timedelta(days=i), (timezone.now() - timezone.timedelta(days=i)).strftime('%Y-%m-%d %H:%M'))
        for i in range(0, 365)
    ]
    last_accident_date = forms.ChoiceField(choices=DATE_CHOICES, label="Дата последнего ДТП")

    # Пострадали ли пассажиры
    PASSENGER_INJURED_CHOICES = [("Да", "Да"), ("Нет", "Нет")]
    passengers_injured = forms.ChoiceField(choices=PASSENGER_INJURED_CHOICES, label="Пострадали ли пассажиры")

    # Поле License plate с примером
    license_plate = forms.CharField(
        max_length=10,
        label="Гос. номер",
        widget=forms.TextInput(attrs={
            'placeholder': 'Пример: А123ВС78'
        })
    )

    # Поле Compensation amount с диапазоном и примером
    compensation_amount = forms.IntegerField(
        label="Сумма выплаты (рубли)",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Пример: 10000 - 750000'
        }),
        min_value=10000,
        max_value=750000
    )
