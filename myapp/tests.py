from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Person
from datetime import datetime

class PersonModelTest(TestCase):
    def test_person_creation_auto_fields(self):
        person = Person.objects.create(
            first_name='Иван',
            last_name='Иванов',
            middle_name='Иванович'
        )
        self.assertIsNotNone(person.passport_series)
        self.assertIsNotNone(person.passport_number)
        self.assertIsNotNone(person.birth_date)
        self.assertIsNotNone(person.city)

    def test_person_manager_from_spb(self):
        Person.objects.create(first_name='Анна', last_name='Петрова', middle_name='Ивановна', city='Санкт-Петербург')
        Person.objects.create(first_name='Иван', last_name='Сидоров', middle_name='Петрович', city='Мурманск')
        spb_persons = Person.objects.from_spb()
        self.assertEqual(spb_persons.count(), 1)
        self.assertEqual(spb_persons.first().city, 'Санкт-Петербург')

class PersonListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.person = Person.objects.create(
            first_name='Петр',
            last_name='Петров',
            middle_name='Петрович',
            birth_date=datetime(2010, 5, 17),
            city='Санкт-Петербург'
        )

    def test_person_list_status_code(self):
        response = self.client.get(reverse('person_list'))
        self.assertEqual(response.status_code, 200)

    def test_person_list_only_spb(self):
        response = self.client.get(reverse('person_list'))
        for person in response.context['persons']:
            self.assertEqual(person.city, 'Санкт-Петербург')

    def test_person_list_context(self):
        response = self.client.get(reverse('person_list'))
        self.assertIn(self.person, response.context['persons'].object_list)

    def test_person_list_content(self):
        response = self.client.get(reverse('person_list'))
        self.assertContains(response, 'Петр')

    def test_person_list_template_content(self):
        response = self.client.get(reverse('person_list'))
        self.assertInHTML(f'<td>Петр</td>', response.content.decode())

    def test_person_list_template_used(self):
        response = self.client.get(reverse('person_list'))
        self.assertTemplateUsed(response, 'myapp/person_list.html')

class URLTests(TestCase):
    def test_person_list_url_exists(self):
        response = self.client.get('/persons/')
        self.assertEqual(response.status_code, 200)
