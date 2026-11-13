from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Contact, Employee


class AppViewsTests(TestCase):
    def test_home_page_renders(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create Account')

    def test_contact_form_saves_data(self):
        response = self.client.post('/contact/', {
            'full_name': 'Jane Doe',
            'email': 'jane@example.com',
            'subject': 'Hello',
            'message': 'This is a test message.'
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Contact.objects.filter(email='jane@example.com').exists())

    def test_employee_list_page_loads(self):
        Employee.objects.create(name='Alice', email='alice@example.com', phone='1234567890')

        response = self.client.get('/show/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alice')

    def test_employee_edit_page_loads(self):
        employee = Employee.objects.create(
            name='Alice',
            email='alice@example.com',
            phone='1234567890',
        )

        response = self.client.get(reverse('edit_employee', args=[employee.id]))
        self.assertEqual(response.status_code, 200)

    def test_user_registration_creates_user(self):
        response = self.client.post('/', {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'StrongPass123',
            'confirm_password': 'StrongPass123',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())
