from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home, book_units, new_unit, new_book, new_element, new_followup, unit_elements, element_followups
from ..models import Book


class LoginRequiredNewBookTests(TestCase):
    def setUp(self):
        #Book.objects.create(title="Testing Django app2", isbn="1234567890983", active=True)
        self.url = reverse('new_book')
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))