from django.db import models
import random
from datetime import datetime, timedelta

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
