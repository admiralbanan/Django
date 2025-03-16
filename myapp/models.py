from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from datetime import datetime, timedelta

class PersonQuerySet(models.QuerySet):
    def from_spb(self):
        return self.filter(city="Санкт-Петербург")

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    passport_series = models.CharField(max_length=4)
    passport_number = models.CharField(max_length=6)
    birth_date = models.DateField()
    city = models.CharField(max_length=50)

    objects = PersonQuerySet.as_manager()

    def save(self, *args, **kwargs):
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

class PersonLog(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=Person)
def log_person_creation(sender, instance, created, **kwargs):
    if created:
        PersonLog.objects.create(person=instance, action='Создан новый пользователь')
