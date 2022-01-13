from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home, book_units, new_unit
from ..models import Book, Unit
from ..forms import NewUnitForm, NewBookForm

class BookUnitTests(TestCase):
    def setUp(self):
        Book.objects.create(title="Testing Django app", isbn="1234567890987", active=True)
        User.objects.create_user(username='john', email='john@doe.com', password='123')
    
    def test_book_units_view_success_status_code(self):
        url = reverse('book_units', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_book_units_view_not_found_status_code(self):
        url = reverse('book_units', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_book_units_url_resolves_book_units_view(self):
        view = resolve('/books/1/')
        self.assertEquals(view.func, book_units)
    
    def test_book_units_view_contains_link_back_to_homepage(self):
        book_units_url = reverse('book_units', kwargs={'pk': 1})
        response = self.client.get(book_units_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

    def test_book_units_view_contains_navigation_links(self):
        book_units_url = reverse('book_units', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_unit_url = reverse('new_unit', kwargs={'pk': 1})

        response = self.client.get(book_units_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_unit_url))
