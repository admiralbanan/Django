from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Person

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

class PersonListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.person = Person.objects.create(
            first_name='Петр',
            last_name='Петров',
            middle_name='Петрович'
        )

    def test_person_list_status_code(self):
        response = self.client.get(reverse('person_list'))
        self.assertEqual(response.status_code, 200)

    def test_person_list_context(self):
        response = self.client.get(reverse('person_list'))
        self.assertIn(self.person, response.context['persons'])

    def test_person_list_template_used(self):
        response = self.client.get(reverse('person_list'))
        self.assertTemplateUsed(response, 'myapp/person_list.html')

    def test_person_list_empty(self):
        Person.objects.all().delete()
        response = self.client.get(reverse('person_list'))
        self.assertEqual(len(response.context['persons']), 0)

    def test_person_list_authenticated_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('person_list'))
        self.assertEqual(response.status_code, 200)

    def test_person_list_anonymous_user(self):
        self.client.logout()
        response = self.client.get(reverse('person_list'))
        self.assertEqual(response.status_code, 200)

    def test_person_list_invalid_url(self):
        response = self.client.get('/invalid_url/')
        self.assertEqual(response.status_code, 404)

    def test_person_list_content(self):
        response = self.client.get(reverse('person_list'))
        self.assertContains(response, self.person.first_name)
        self.assertContains(response, self.person.last_name)

    def test_person_list_template_content(self):
        response = self.client.get(reverse('person_list'))
        self.assertInHTML(f'<td>{self.person.first_name}</td>', response.content.decode())
        self.assertInHTML(f'<td>{self.person.last_name}</td>', response.content.decode())

class URLTests(TestCase):
    def test_person_list_url_exists(self):
        response = self.client.get('/persons/')
        self.assertEqual(response.status_code, 200)
