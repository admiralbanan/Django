from django.db import models
import random
from datetime import datetime, timedelta
import string
from django.utils import timezone

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    passport_series = models.CharField(max_length=4)
    passport_number = models.CharField(max_length=6)
    birth_date = models.DateField()
    city = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        # Генерация данных при сохранении, если поля пустые
        if not self.passport_series:
            self.passport_series = f"{random.randint(38, 42)}{random.randint(10, 99)}"
        if not self.passport_number:
            self.passport_number = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        if not self.birth_date:
            start_date = datetime(1999, 1, 1)
            end_date = datetime(2015, 1, 1)
            self.birth_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        if not self.city:
            cities = [
                "Санкт-Петербург", "Архангельск", "Мурманск", "Петрозаводск",
                "Вологда", "Череповец", "Великий Новгород", "Псков",
                "Калининград", "Сыктывкар"
            ]
            self.city = random.choice(cities)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.city})"


class CarAccident(models.Model):
    CAR_BRANDS = [
        "Lada", "Gaz", "Kamaz", "BMW", "Mercedes", "Audi", "Volkswagen",
        "Renault", "Peugeot", "Opel", "Skoda", "Fiat"
    ]
    
    RUSSIAN_REGIONS = [10, 77, 78, 99, 22, 42, 55, 61, 99, 197, 198]  # список регионов (можете расширить его)
    
    brand = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=10)
    year_of_manufacture = models.IntegerField()
    last_accident_date = models.DateTimeField()
    compensation_amount = models.IntegerField()
    passengers_injured = models.CharField(max_length=3)

    def save(self, *args, **kwargs):
        if not self.brand:
            self.brand = random.choice(self.CAR_BRANDS)
        
        if not self.license_plate:
            letters = random.choices(string.ascii_uppercase, k=3)
            numbers = f"{random.randint(1, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
            region = random.choice(self.RUSSIAN_REGIONS)
            self.license_plate = f"{letters[0]}{numbers}{letters[1]}{letters[2]}{region}"

        if not self.year_of_manufacture:
            self.year_of_manufacture = random.randint(2001, 2024)
        
        # if not self.last_accident_date:
        #     now = datetime.now()
        #     self.last_accident_date = now - timedelta(days=random.randint(0, 365))
        
        if not self.last_accident_date:
            now = timezone.now()
            self.last_accident_date = now - timezone.timedelta(days=random.randint(0, 365))

        if not self.compensation_amount:
            self.compensation_amount = random.randint(10000, 750000)
        
        if not self.passengers_injured:
            self.passengers_injured = random.choice(["Да", "Нет"])
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.brand} ({self.license_plate})"